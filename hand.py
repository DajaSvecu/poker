from card import Card
from typing import List

class Hand:
    def __init__(self, cards: List[Card]) -> None:
        self.cards = cards

    def __str__(self) -> str:
        return " ".join([str(card) for card in self.cards])
    
    def is_flush(self):
        suits = [card.get_suit() for card in self.cards]
        return len(set(suits)) == 1
    
    def is_straight(self):
        ranks = sorted([card.get_rank() for card in self.cards])
        for i in range(len(ranks)-1):
            if ranks[i]+1 != ranks[i+1]:
                return False
        return True

    
c1 = Card("2", "H")
c2= Card("3", "S")
c3= Card("4", "D")
h = Hand([c3,c2,c2])
print(h.is_straight())
