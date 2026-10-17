"""Regression checks for the narrow WD-35 restoration guard."""
import unittest
from pathlib import Path

class WD35GuardTests(unittest.TestCase):
    def test_only_one_exact_source_target_pair(self):
        source = Path("watchdog/check.py").read_text()
        self.assertIn("bf3f3d85413deb94c1b36eee3ea4aabd414cddee", source)
        self.assertIn("e317b1c42668126141baecd797cad84b4a1d57fe", source)
        self.assertIn('name == "manifests/BASELINE-c498e84.sha256"', source)
        self.assertIn('failures.append(f"W4 rewritten manifest', source)

    def test_authorization_marker_is_exact(self):
        marker = Path("manifests/W4_RESTORATIONS.txt").read_text().splitlines()
        self.assertEqual(len(marker), 1)
        self.assertEqual(marker[0], "WD-35 manifests/BASELINE-c498e84.sha256 "
                         "bf3f3d85413deb94c1b36eee3ea4aabd414cddee "
                         "e317b1c42668126141baecd797cad84b4a1d57fe")

if __name__ == "__main__":
    unittest.main()
