"""WD-03 focused unit tests. Integration fixtures and CI still pending."""
import importlib.util
import tempfile
import unittest
from pathlib import Path

spec = importlib.util.spec_from_file_location("a25_watchdog", Path(__file__).with_name("check.py"))
watchdog = importlib.util.module_from_spec(spec)
spec.loader.exec_module(watchdog)


class WatchdogCoreTests(unittest.TestCase):
    def test_protected_paths(self):
        self.assertTrue(watchdog.protected("roundtable/inbox/a.md"))
        self.assertTrue(watchdog.protected("archives/claude/inbox/a.md"))
        self.assertTrue(watchdog.protected("legacy/pockettest/a.md"))
        self.assertFalse(watchdog.protected("roundtable/sessions/a.md"))
        self.assertFalse(watchdog.protected("archives/claude/outbox/a.md"))

    def test_record_id_suffix(self):
        self.assertEqual(watchdog.canonical("case-studies/A25-F-002-incident.md", ""), "A25-F-002")
        self.assertEqual(watchdog.canonical("case-studies/A25-F-001-CORR-001.md", ""), "A25-F-001-CORR-001")
        self.assertEqual(watchdog.canonical("living-record/A25-DEC-001-resolution.md",
                                           "---\nid: A25-DEC-001-RESOLUTION\n---"),
                         "A25-DEC-001-RESOLUTION")

    def test_template_not_id(self):
        self.assertIsNone(watchdog.canonical("templates/example.md", "---\nid: A25-F-UNASSIGNED\n---"))

    def test_frontmatter_disagreement(self):
        self.assertTrue(watchdog.canonical("case-studies/A25-F-004-x.md",
                                            "---\nid: A25-F-002\n---").startswith("!MISMATCH:"))

    def test_path_traversal(self):
        self.assertIsNone(watchdog.safe_path("../outside"))
        self.assertIsNone(watchdog.safe_path("/etc/passwd"))


if __name__ == "__main__":
    unittest.main()
