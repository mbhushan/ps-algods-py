class Card(object):
    """ Represents a standard playing card.
    Attributes:
        suit: Integer 0-3
        rank: Integer 1-13
    """

    suit_names = ["Clubs", "Diamonds", "Hearts", "Spades"]
    rank_names = [None, "2", "3", "4", "5", "6", "7", "8",
                  "9", "10", "Jack", "Queen", "King", "Ace"]

    def __init__(self, suit=0, rank=1):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        """ returns a human readable string representation """
        return '%s of %s' % (Card.rank_names[self.rank],
                             Card.suit_names[self.suit])

    def __lt__(self, other):
        """ Compares this card to other, only by rank (no suit comparison)
        Returns a positive number if this > other, negative otherwise.
        Returns 0 if the cards are of same rank
        """
        # t1 = self.rank
        # t2 = other.rank
        t1 = self.suit, self.rank
        t2 = other.suit, other.rank
        return t1 < t2

    def getRank(self):
        return self.rank
