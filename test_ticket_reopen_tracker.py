import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import unittest
from main import rates


def row(c, s):
    return {"ticket": "T1", "category": c, "status": s}


class TestReopenRates(unittest.TestCase):
    def test_rate_computed(self):
        result = rates([row("VPN", "closed"), row("VPN", "reopened")])
        self.assertEqual(result[0][1], 0.5)

    def test_highest_first(self):
        result = rates([row("A", "closed"), row("B", "reopened"), row("B", "closed")])
        self.assertEqual(result[0][0], "B")

    def test_small_sample_flagged(self):
        result = rates([row("VPN", "closed")])
        self.assertIn("small sample", result[0][3])

    def test_zero_reopens(self):
        result = rates([row("VPN", "closed"), row("VPN", "open")])
        self.assertEqual(result[0][1], 0.0)
