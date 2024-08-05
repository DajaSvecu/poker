class Card:
    __ranks = (
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "J",
        "Q",
        "K",
        "A",
    )
    __suits = ("C", "D", "H", "S")

    def __init__(self, rank: str, suit: str) -> None:
        self.rank = rank
        self.suit = suit

    def __str__(self) -> str:
        return f"{self.rank}{self.suit}"

    def get_rank(self) -> int:
        return self.__ranks.index(self.rank)

    def get_suit(self) -> int:
        return self.__suits.index(self.suit)
