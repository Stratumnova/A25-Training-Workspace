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
