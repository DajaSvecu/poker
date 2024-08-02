import unittest
from hand import Hand
from card import Card

class TestHand(unittest.TestCase):
    def test_str(self):
        h = Hand([
            Card("2","D"),
            Card("3","S"),
            Card("5","H"),
        ])
        self.assertIsInstance(str(h), str)
