from card import Card
from typing import List
from collections import Counter

class PokerHand:
    def __init__(self, cards: List[Card]) -> None:
        if len(cards) != 5:
            raise ValueError("Poker hand has to contain 5 cards!")
        self.cards = cards

    def __str__(self) -> str:
        return " ".join([str(card) for card in self.cards])
    
    def flush(self):
        suits = [card.get_suit() for card in self.cards]
        return len(set(suits)) == 1
    
    def straight(self):
        ranks = sorted([card.get_rank() for card in self.cards])
        for i in range(len(ranks)-1):
            if ranks[i]+1 != ranks[i+1]:
                return False
        return True
    
    @staticmethod
    def of_a_kind(cards: List[Card], number: int) -> bool:
        rank_counter = Counter([card.get_rank() for card in cards])
        for rank in rank_counter:
            if rank_counter[rank] == number:
                return True
        return False
    
    def four_of_a_kind(self) -> bool:
        return self.of_a_kind(self.cards, 4)
    
    def three_of_a_kind(self) -> bool:
        return self.of_a_kind(self.cards, 3)
    
    def two_of_a_kind(self) -> bool:
        return self.of_a_kind(self.cards, 2)

    def full_house(self) -> bool:
        return self.three_of_a_kind() and self.two_of_a_kind()

    def two_pair(self) -> bool:
        rank_counter = Counter([card.get_rank() for card in self.cards])
        for _, count in rank_counter.most_common(2):
            if count != 2:
                return False
        return True

    def high_card(self) -> int:
        return max(self.cards, key=lambda x: x.get_rank()).get_rank()
