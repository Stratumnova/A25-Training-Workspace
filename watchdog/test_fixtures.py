"""WD-03 isolated git-repository integration fixtures.

These tests create disposable local repositories. They never modify A25 records.
"""
import importlib.util
import hashlib
import subprocess
import tempfile
import unittest
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
from unittest.mock import patch

spec = importlib.util.spec_from_file_location("a25_watchdog", Path(__file__).with_name("check.py"))
wd = importlib.util.module_from_spec(spec)
spec.loader.exec_module(wd)


class WatchdogRepositoryFixtures(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.previous_root = wd.ROOT
        wd.ROOT = self.root
        self.addCleanup(lambda: setattr(wd, "ROOT", self.previous_root))
        self.git("init", "-q")
        self.git("config", "user.name", "WD fixture")
        self.git("config", "user.email", "fixture@example.invalid")
        self.write("roundtable/inbox/message.md", self.message())
        self.write("manifests/baseline.sha256", self.manifest("roundtable/inbox/message.md"))
        self.commit()

    def git(self, *args):
        return subprocess.run(["git", "-C", str(self.root), *args], check=True,
                              stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    def write(self, name, content):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")

    def message(self):
        return ("**FROM:** Fixture\n**FOR:** Reviewer\n**DATE:** time unknown\n"
                "**RE:** Check\n**BASIS:** Fixture\n")

    def manifest(self, name):
        digest = hashlib.sha256((self.root / name).read_bytes()).hexdigest()
        return f"{digest}  {name}\n"

    def commit(self):
        self.git("add", "-A")
        self.git("commit", "-qm", "fixture state")

    def check(self):
        out = StringIO()
        with redirect_stdout(out):
            code = wd.run()
        return code, out.getvalue()

    def test_clean_baseline(self):
        status, report = self.check()
        self.assertEqual(status, 0, report)

    def test_modified_inbox_byte(self):
        self.write("roundtable/inbox/message.md", self.message() + "altered\n")
        self.commit()
        status, report = self.check()
        self.assertEqual(status, 1)
        self.assertIn("W1 hash mismatch", report)
        self.assertIn("W4 protected change", report)

    def test_deleted_listed_file(self):
        (self.root / "roundtable/inbox/message.md").unlink()
        self.commit()
        status, report = self.check()
        self.assertEqual(status, 1)
        self.assertIn("W1 missing/unsafe", report)

    def test_unlisted_inbox(self):
        self.write("roundtable/inbox/new.md", self.message())
        self.commit()
        status, report = self.check()
        self.assertEqual(status, 1)
        self.assertIn("W2 unmanifested", report)

    def test_missing_date(self):
        self.write("roundtable/inbox/new.md", self.message().replace("**DATE:** time unknown\n", ""))
        self.write("manifests/baseline.sha256",
                   (self.root / "manifests/baseline.sha256").read_text()
                   + self.manifest("roundtable/inbox/new.md"))
        self.commit()
        status, report = self.check()
        self.assertEqual(status, 1)
        self.assertIn("W3", report)

    def test_duplicate_id(self):
        self.write("case-studies/A25-F-007-first.md", "first\n")
        self.write("case-studies/A25-F-007-second.md", "second\n")
        self.commit()
        status, report = self.check()
        self.assertEqual(status, 1)
        self.assertIn("W5 collision", report)

    def test_modified_legacy(self):
        self.write("legacy/old.md", "original\n")
        self.write("manifests/baseline.sha256",
                   (self.root / "manifests/baseline.sha256").read_text()
                   + self.manifest("legacy/old.md"))
        self.commit()
        self.write("legacy/old.md", "changed\n")
        self.commit()
        status, report = self.check()
        self.assertEqual(status, 1)
        self.assertIn("W4 protected change", report)

    def test_multi_commit_push_detects_intermediate_protected_change(self):
        # Final tree is clean, but the first commit in the push rewrote history.
        before = self.git("rev-parse", "HEAD").stdout.decode().strip()
        self.write("roundtable/inbox/message.md", self.message() + "tampered\\n")
        self.commit()
        self.write("roundtable/inbox/message.md", self.message())
        self.commit()
        with patch.dict("os.environ", {"A25_WD_BEFORE": before}):
            status, report = self.check()
        self.assertEqual(status, 1, report)
        self.assertIn("W4 protected change", report)

    def test_multi_commit_push_detects_intermediate_manifest_rewrite(self):
        before = self.git("rev-parse", "HEAD").stdout.decode().strip()
        original = (self.root / "manifests/baseline.sha256").read_text()
        self.write("manifests/baseline.sha256", "0" * 64 + "  roundtable/inbox/message.md\\n")
        self.commit()
        self.write("manifests/baseline.sha256", original)
        self.commit()
        with patch.dict("os.environ", {"A25_WD_BEFORE": before}):
            status, report = self.check()
        self.assertEqual(status, 1, report)
        self.assertIn("W4 rewritten manifest", report)

    def test_workflow_write_permission_rejected(self):
        self.write(".github/workflows/example.yml",
                   "name: test\non: push\npermissions:\n  contents: read\n"
                   "jobs:\n  example:\n    permissions:\n      issues: write\n")
        self.commit()
        status, report = self.check()
        self.assertEqual(status, 1, report)
        self.assertIn("W6 write permission", report)

    def test_frontmatter_id_must_be_top_level(self):
        sample = "---\ntitle: sample\nnotes: |\n  id: A25-F-999\n---\n"
        self.assertIsNone(wd.canonical("notes/ordinary.md", sample))

    def test_correction_frontmatter_specificity(self):
        sample = "---\nid: A25-F-001-CORR-001\n---\n"
        self.assertEqual(wd.canonical("case-studies/A25-F-001-correction-001.md", sample),
                         "A25-F-001-CORR-001")

    def test_malformed_digest(self):
        self.write("manifests/baseline.sha256", "xyz  roundtable/inbox/message.md\n")
        self.commit()
        status, report = self.check()
        self.assertEqual(status, 1)
        self.assertIn("W1 malformed", report)

    def test_rewritten_manifest_line(self):
        self.write("manifests/baseline.sha256", "0" * 64 + "  roundtable/inbox/message.md\n")
        self.commit()
        status, report = self.check()
        self.assertEqual(status, 1)
        self.assertIn("W4 rewritten manifest", report)

    def test_new_inbox_with_manifest(self):
        self.write("roundtable/inbox/new.md", self.message())
        self.write("manifests/baseline.sha256",
                   (self.root / "manifests/baseline.sha256").read_text()
                   + self.manifest("roundtable/inbox/new.md"))
        self.commit()
        status, report = self.check()
        self.assertEqual(status, 0, report)

    def test_new_session_with_headers(self):
        self.write("roundtable/sessions/2026-10-16/RT-099-fixture.md", self.message())
        self.commit()
        status, report = self.check()
        self.assertEqual(status, 0, report)


if __name__ == "__main__":
    unittest.main()
