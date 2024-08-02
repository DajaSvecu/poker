class Card:
    __ranks = {
        "2":1,
        "3":2,
        "4":3,
        "5":4,
        "6":5,
        "7":6,
        "8":7,
        "9":8,
        "10":9,
        "J":10,
        "Q":11,
        "K":12,
        "A":13,
    }
    __suits = {
        "C": 1,
        "D": 2,
        "H": 3,
        "S": 4,
    }
    def __init__(self, rank:str, suit:str) -> None:
        self.rank = rank
        self.suit = suit

    def __str__(self) -> str:
        return f"{self.rank}{self.suit}"
    
    def get_rank(self) -> int:
        return self.__ranks[self.rank]
    
    def get_suit(self) -> int:
        return self.__suits[self.suit]