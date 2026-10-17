import unittest
from registry import Registry,Ledger,Denied,parse_id
S={"repo":"SYNTHETIC/fixtures","commit":"a"*40,"path":"fake/example"}
class Tests(unittest.TestCase):
 def denied(self,f):
  with self.assertRaises(Denied):f()
 def test_gate01_collision(self):
  r=Registry()
  for sub,kind in [("PS","TEST"),("TRAIN","DOC")]:r.add(r.reserve(sub,kind),S,"PUBLIC","Gate-01")
  self.assertEqual(len(r.search("Gate-01")),2)
 def test_key5_prompt_vs_code(self):
  r=Registry()
  for sub,kind in [("LORE","PROMPT"),("PS","CODE")]:r.add(r.reserve(sub,kind),S,"PUBLIC","Key5")
  self.assertEqual(len(set(x["id"] for x in r.search("Key5"))),2)
 def test_seat_impersonation(self):
  r=Registry();i=r.reserve("NS","TEST");self.denied(lambda:r.add(i,S,"PUBLIC",assigned_seat="gpt",principal="claude"))
 def test_revision_conflict(self):
  r=Registry();i=r.reserve("NS","DOC");r.add(i,S,"PUBLIC");r.revise(i,1,S);self.denied(lambda:r.revise(i,1,S))
 def test_fake_token_denied_and_scoped(self):
  r=Registry();i=r.reserve("NS","DATA");r.add(i,S,"TEST-SENSITIVE")
  self.denied(lambda:r.retrieve(i))
  self.assertEqual(r.retrieve(i,"approved-tester","isolated-leak-test","A25_FAKE_TOKEN_DO_NOT_USE_001")["id"],i)
 def test_invalid_grammar(self):
  for v in ["A25:PS:TEST:X","A25:PS:TEST:N000001@r0","A25:PS:TEST:N000001@r01","A25:ps:TEST:N000001"]:
   self.denied(lambda v=v:parse_id(v))
 def test_missing_source(self):
  r=Registry();i=r.reserve("NS","DOC");self.denied(lambda:r.add(i,{},"PUBLIC"))
 def test_duplicate_id(self):
  r=Registry();i=r.reserve("NS","DOC");r.add(i,S,"PUBLIC");self.denied(lambda:r.add(i,S,"PUBLIC"))
 def test_unreserved_claim(self):
  self.denied(lambda:Registry().add("A25:NS:DOC:N000001",S,"PUBLIC"))
 def test_ledger_rewrite(self):
  l=Ledger();l.append("x","DISCOVERED","fixture","a"*40)
  e=l.events;e[0]["state"]="ACCEPTED";self.assertEqual(l.events[0]["state"],"DISCOVERED")
  self.denied(lambda:l.append("x","DISCOVERED","fixture","a"*40,expected="DISCOVERED"))
 def test_ledger_hash_conflict(self):
  self.denied(lambda:Ledger().append("x","DISCOVERED","fixture","a"*40,expected_digest="a",observed_digest="b"))
 def test_ledger_source_drift(self):
  l=Ledger();l.append("x","DISCOVERED","fixture","a"*40)
  self.denied(lambda:l.append("x","CLASSIFIED","fixture","b"*40,classification="PUBLIC",expected="DISCOVERED"))
 def test_public_projection(self):
  r=Registry()
  for c in ("PUBLIC","UNKNOWN"):r.add(r.reserve("NS","DATA"),S,c,"test")
  self.assertEqual(len(r.search("test")),1)
 def test_ledger_classification(self):
  l=Ledger();l.append("x","DISCOVERED","fixture","a"*40)
  self.denied(lambda:l.append("x","CLASSIFIED","fixture","a"*40,classification="BAD",expected="DISCOVERED"))
if __name__=="__main__":unittest.main()
