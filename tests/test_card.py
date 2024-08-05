import unittest

from card import Card


class TestCard(unittest.TestCase):
    def setUp(self) -> None:
        self.rank = "K"
        self.suit = "S"
        self.card = Card(self.rank, self.suit)

        return super().setUp()

    def test_str(self):
        self.assertEqual(str(self.card), f"{self.rank}{self.suit}")

    def test_get_rank(self):
        self.assertEqual(self.card.get_rank(), 11)

    def test_get_suit(self):
        self.assertEqual(self.card.get_suit(), 3)
