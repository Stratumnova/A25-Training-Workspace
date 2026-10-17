"""A25-NS-O002 synthetic, single-writer, in-memory namespace prototype."""
import re, json, hashlib
SUBSYSTEMS=set("ARC PS WD NS TOOLS HA LORE TRAIN".split())
KINDS=set("DOC SPEC CODE TEST EVENT CONCEPT PERSONA DATA REPORT ORDER LEDGER PROMPT CONFIG ASSET BINARY ARCHIVE".split())
CLASSES=set("PUBLIC TEST-SENSITIVE TEAM-RESTRICTED REAL-PRIVATE UNKNOWN".split())
STATES="DISCOVERED CLASSIFIED MAPPED PORTED VERIFIED ACCEPTED LEGACY-ARCHIVED".split()
PATTERN=re.compile(r"A25:([A-Z][A-Z0-9]{1,15}):([A-Z][A-Z0-9]{1,15}):([A-Z][A-Z0-9]{3,12})(?:@r([1-9][0-9]*))?")
class Denied(ValueError): pass
def parse_id(value):
    m=PATTERN.fullmatch(value) if isinstance(value,str) else None
    if not m: raise Denied("invalid ID")
    sub,kind,local,rev=m.groups()
    if sub not in SUBSYSTEMS or kind not in KINDS: raise Denied("unknown namespace")
    return ":".join(("A25",sub,kind,local)),int(rev) if rev else None
class Registry:
    def __init__(self): self.records={};self.reserved=set();self.counter={};self.aliases=[]
    def reserve(self,sub,kind):
        parse_id(f"A25:{sub}:{kind}:N000001")
        k=(sub,kind);self.counter[k]=self.counter.get(k,0)+1
        value=f"A25:{sub}:{kind}:N{self.counter[k]:06d}";self.reserved.add(value);return value
    def add(self,logical,source,classification,alias=None,revision=1,assigned_seat=None,principal=None,author=None,narrative=None):
        base,rev=parse_id(logical)
        if rev or base in self.records or base not in self.reserved: raise Denied("duplicate or unreserved")
        if revision!=1 or classification not in CLASSES: raise Denied("invalid revision/classification")
        if not isinstance(source,dict) or not all(source.get(k) for k in ("repo","commit","path")): raise Denied("missing source")
        if not re.fullmatch("[a-f0-9]{40}",source["commit"]): raise Denied("unresolved commit")
        if assigned_seat and principal and assigned_seat!=principal: raise Denied("seat impersonation")
        self.records[base]={"id":base,"revision":1,"source":dict(source),"classification":classification,"assigned_seat":assigned_seat,"principal":principal,"source_author":author,"narrative_identity":narrative}
        self.reserved.remove(base)
        if alias is not None:self.aliases.append((alias,base))
        return base+"@r1"
    def revise(self,base,expected,source):
        if base not in self.records or self.records[base]["revision"]!=expected: raise Denied("revision conflict")
        if not all(source.get(k) for k in ("repo","commit","path")): raise Denied("missing source")
        self.records[base]["revision"]+=1;self.records[base]["source"]=dict(source)
        return base+"@r"+str(self.records[base]["revision"])
    def search(self,term):
        return [{"id":i+"@r"+str(self.records[i]["revision"]),"alias":a,"source_context":self.records[i]["source"]["repo"]} for a,i in self.aliases if a==term and self.records[i]["classification"]=="PUBLIC"]
    def retrieve(self,id,principal=None,purpose="normal",fixture=None):
        if id not in self.records: raise Denied("missing record")
        rec=self.records[id];c=rec["classification"]
        if c in ("UNKNOWN","REAL-PRIVATE"): raise Denied("deny default")
        if c=="TEAM-RESTRICTED" and principal!="approved-builder":raise Denied("restricted")
        if c=="TEST-SENSITIVE" and not (principal=="approved-tester" and purpose=="isolated-leak-test" and fixture=="A25_FAKE_TOKEN_DO_NOT_USE_001"):raise Denied("fixture withheld")
        return dict(rec)
class Ledger:
    """Append-only in process only. No durable transaction or tamper-proof store."""
    def __init__(self):self._events=[]
    @property
    def events(self):return tuple(json.loads(json.dumps(e)) for e in self._events)
    def append(self,key,state,evidence,source_revision,classification="UNKNOWN",expected=None,destination_revision=None,expected_digest=None,observed_digest=None):
        if state not in STATES or classification not in CLASSES:raise Denied("bad state/class")
        if not evidence or not source_revision:raise Denied("missing evidence")
        if expected_digest and observed_digest and expected_digest!=observed_digest:raise Denied("hash conflict")
        previous=[e for e in self._events if e["key"]==key];old=previous[-1]["state"] if previous else None
        if old!=expected or (old is None and state!="DISCOVERED") or (old is not None and STATES.index(state)!=STATES.index(old)+1):raise Denied("illegal transition")
        if previous and previous[-1]["source_revision"]!=source_revision:raise Denied("source drift")
        if classification in ("UNKNOWN","REAL-PRIVATE") and state not in ("DISCOVERED","CLASSIFIED"):raise Denied("unclassified")
        if state in STATES[3:] and not destination_revision:raise Denied("missing destination revision")
        event={"key":key,"state":state,"source_revision":source_revision,"destination_revision":destination_revision,"classification":classification,"evidence":evidence,"sequence":len(self._events)+1}
        event["digest"]=hashlib.sha256(json.dumps(event,sort_keys=True).encode()).hexdigest()
        self._events.append(event);return dict(event)
