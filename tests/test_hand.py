import unittest

from card import Card
from hand import PokerHand


class TestPokerHand(unittest.TestCase):
    def setUp(self) -> None:
        self.straight_flush = PokerHand([Card(str(x), "D") for x in range(2, 7)])
        self.poker = PokerHand(
            [
                Card("A", "D"),
                Card("A", "S"),
                Card("A", "H"),
                Card("A", "C"),
                Card("K", "D"),
            ]
        )
        self.full_house = PokerHand(
            [
                Card("A", "D"),
                Card("A", "S"),
                Card("A", "H"),
                Card("K", "C"),
                Card("K", "D"),
            ]
        )
        self.two_pair = PokerHand(
            [
                Card("A", "D"),
                Card("A", "S"),
                Card("2", "H"),
                Card("K", "C"),
                Card("K", "D"),
            ]
        )
        return super().setUp()

    def test_less_than_5_cards(self):
        with self.assertRaises(ValueError) as context:
            hand = PokerHand([Card("2", "D") for _ in range(4)])

    def test_more_than_5_cards(self):
        with self.assertRaises(ValueError) as context:
            hand = PokerHand([Card("2", "D") for _ in range(6)])

    def test_str(self):
        hand = PokerHand([Card("2", "D") for _ in range(5)])
        self.assertIsInstance(str(hand), str)

    def test_straight(self):
        self.assertTrue(self.straight_flush.straight())

    def test_flush(self):
        self.assertTrue(self.straight_flush.flush())

    def test_four_of_a_kind(self):
        self.assertTrue(self.poker.four_of_a_kind())

    def test_three_of_a_kind(self):
        self.assertTrue(self.full_house.three_of_a_kind())

    def test_two_of_a_kind(self):
        self.assertTrue(self.full_house.two_of_a_kind())

    def test_two_pair(self):
        self.assertTrue(self.two_pair.two_pair())

    def test_high_card(self):
        self.assertEqual(self.two_pair.high_card(), 12)
