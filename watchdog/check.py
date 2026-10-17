#!/usr/bin/env python3
"""A25 Watchdog v0: read-only deterministic repository checks.

WD-02 implementation draft. Run at repository root. No writes or execution of
repository content. Exit 1 for FAIL, 0 for PASS/WARN/SKIPPED.
"""
from __future__ import annotations

import hashlib
import os
import re
import subprocess
import sys
from pathlib import Path, PurePosixPath

ROOT = Path(__file__).resolve().parents[1]
DIGEST = re.compile(r"^([0-9a-fA-F]{64})  (.+)$")
FIELDS = ("FROM", "FOR", "DATE", "RE", "BASIS")
ID = re.compile(r"^(A25-[A-Z]+-\d{3}(?:-CORR-\d{3}|-RESOLUTION)?|RT-\d{3}|WD-\d{3})")
FRONT = re.compile(r'^id:\s*[\x27\x22]?([^\s\x27\x22]+)', re.MULTILINE)
PROTECTED = ("roundtable/inbox/", "legacy/")


def git(*args: str) -> bytes:
    return subprocess.check_output(["git", "-C", str(ROOT), *args], stderr=subprocess.DEVNULL)


def protected(path: str) -> bool:
    parts = PurePosixPath(path).parts
    return path.startswith(PROTECTED) or (
        len(parts) >= 3 and parts[0] == "archives" and parts[2] == "inbox"
    )


def safe_path(raw: str) -> Path | None:
    p = PurePosixPath(raw)
    if p.is_absolute() or not p.parts or any(x in ("..", ".") for x in p.parts):
        return None
    candidate = ROOT.joinpath(*p.parts)
    if not candidate.resolve().is_relative_to(ROOT.resolve()):
        return None
    if any(q.is_symlink() for q in (candidate, *candidate.parents) if q != ROOT):
        return None
    return candidate


def canonical(path: str, contents: str) -> str | None:
    block = contents.split("---", 2)[1] if contents.startswith("---") and contents.count("---") >= 2 else ""
    m = FRONT.search(block)
    front = m.group(1) if m else None
    file_id = ID.match(Path(path).stem.upper())
    fm_id = ID.match(front) if front else None
    if front and ("UNASSIGNED" in front):
        return None
    if fm_id and file_id and not (fm_id.group(1) == file_id.group(1) or fm_id.group(1).startswith(file_id.group(1) + "-")):
        # Frontmatter can intentionally be more specific; disagreements need review.
        return "!MISMATCH:" + fm_id.group(1) + ":" + file_id.group(1)
    return fm_id.group(1) if fm_id else file_id.group(1) if file_id else None


def run() -> int:
    failures, warnings = [], []
    try:
        tracked = set(git("ls-files", "-z").decode().strip("\0").split("\0"))
    except (subprocess.CalledProcessError, UnicodeDecodeError):
        print("FAIL: cannot list tracked files")
        return 1
    covered = set()
    manifests = sorted(p for p in tracked if p.startswith("manifests/") and p.endswith(".sha256"))
    for name in manifests:
        file = safe_path(name)
        if file is None or not file.is_file():
            failures.append(f"W1 unsafe/missing manifest {name}")
            continue
        for number, line in enumerate(file.read_text(encoding="utf-8").splitlines(), 1):
            m = DIGEST.fullmatch(line)
            if not m:
                failures.append(f"W1 malformed {name}:{number}")
                continue
            digest, target = m.groups()
            p = safe_path(target)
            if p is None or not p.is_file() or target not in tracked:
                failures.append(f"W1 missing/unsafe {target}")
                continue
            if hashlib.sha256(p.read_bytes()).hexdigest() != digest.lower():
                failures.append(f"W1 hash mismatch {target}")
            covered.add(target)
    for name in sorted(tracked):
        if protected(name) and name not in covered:
            failures.append(f"W2 unmanifested {name}")
    # Header exceptions are exact paths, each line: relative/path.md<TAB>reason.
    exemptions = {}
    exempt_file = ROOT / "manifests/W3_EXEMPT.txt"
    if exempt_file.exists():
        for line in exempt_file.read_text(encoding="utf-8").splitlines():
            if not line.strip() or line.startswith("#"):
                continue
            fields = line.split("\t", 1)
            if len(fields) != 2 or not fields[1].strip() or safe_path(fields[0]) is None:
                failures.append("W3 malformed exemption")
            else:
                exemptions[fields[0]] = fields[1]
    for name in sorted(tracked):
        if not name.endswith(".md") or not name.startswith(("roundtable/sessions/", "roundtable/inbox/")):
            continue
        path = safe_path(name)
        if path is None or not path.is_file():
            failures.append(f"W3 unsafe/missing {name}")
            continue
        lines = path.read_text(encoding="utf-8", errors="replace").splitlines()[:15]
        found = set()
        for line in lines:
            cleaned = line.strip().replace("**", "").replace("__", "")
            for field in FIELDS:
                if re.search(rf"(?:^|\s[·|]\s){field}:\s*\S", cleaned):
                    found.add(field)
        missing = set(FIELDS) - found
        if missing:
            (warnings if name in exemptions else failures).append(f"W3 {name}: {','.join(sorted(missing))}")
    ids = {}
    for name in sorted(tracked):
        if not name.endswith(".md"):
            continue
        path = safe_path(name)
        if path is None or not path.is_file():
            continue
        if name.startswith("roundtable/inbox/") and re.match(r"RT-\d{3}", Path(name).name):
            continue  # replies reference session IDs; sessions own them
        record = canonical(name, path.read_text(encoding="utf-8", errors="replace"))
        if record and record.startswith("!MISMATCH"):
            failures.append(f"W5 {name}: {record}")
        elif record:
            ids.setdefault(record, []).append(name)
    for record, paths in sorted(ids.items()):
        if len(paths) > 1:
            # Historical F-002 exception requires exact known paths AND
            # additive correction with the canonical replacement ID.
            historical = {
                "case-studies/A25-F-002-safety-stop-rt005-index-2026-10-16.md",
                "legacy/pockettest/a25-training/case-studies/A25-F-002-proposed-gpt-fork-sandbox.md",
            }
            correction = ROOT / "case-studies/A25-F-004-correction-rt005-safety-stop-id-2026-10-16.md"
            if (record == "A25-F-002" and set(paths) == historical
                    and correction.is_file()
                    and all(x in correction.read_text(encoding="utf-8") for x in historical)
                    and "A25-F-004" in correction.read_text(encoding="utf-8")):
                warnings.append(f"W5 historical corrected collision {record}: {'; '.join(paths)}")
            else:
                failures.append(f"W5 collision {record}: {'; '.join(paths)}")
    try:
        parents = git("rev-list", "--parents", "-n", "1", "HEAD").decode().strip().split()
        if len(parents) < 2:
            warnings.append("W4 SKIPPED root commit")
        else:
            changes = git("diff", "--no-renames", "--name-status", "-z", parents[1], "HEAD").decode().split("\0")
            for i in range(0, len(changes)-1, 2):
                status, name = changes[i], changes[i+1]
                if status[:1] in ("M", "D") and protected(name):
                    failures.append(f"W4 protected change {status} {name}")
                elif name.startswith("manifests/") and status[:1] in ("M", "D"):
                    if status[:1] == "D":
                        failures.append(f"W4 deleted manifest {name}")
                    else:
                        try:
                            previous = git("show", f"{parents[1]}:{name}")
                            current = (ROOT / name).read_bytes()
                            if not current.startswith(previous):
                                failures.append(f"W4 rewritten manifest {name}")
                        except (OSError, subprocess.CalledProcessError):
                            failures.append(f"W4 cannot verify manifest append {name}")
    except (subprocess.CalledProcessError, UnicodeDecodeError):
        failures.append("W4 cannot compare first parent")
    for name in sorted(tracked):
        if not name.startswith(".github/workflows/") or not name.endswith((".yml", ".yaml")):
            continue
        p = safe_path(name)
        if p is None or not p.is_file():
            failures.append(f"W6 unsafe workflow {name}")
            continue
        data = p.read_text(encoding="utf-8")
        if re.search(r"(?m)^\s*pull_request_target\s*:", data):
            failures.append(f"W6 forbidden trigger {name}")
        if re.search(r"(?m)^\s*secrets\s*:", data) or "${{ secrets." in data:
            failures.append(f"W6 secret reference {name}")
        if not re.search(r"(?m)^\s*contents:\s*read\s*$", data):
            failures.append(f"W6 missing contents: read {name}")
    for message in failures:
        print("FAIL:", message)
    for message in warnings:
        print("WARN:", message)
    print(f"WD-02 draft: {len(failures)} FAIL, {len(warnings)} WARN")
    return int(bool(failures))


if __name__ == "__main__":
    sys.exit(run())
