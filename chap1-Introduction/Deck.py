from Card import Card
import random


class Deck(object):
    """ Represents a deck of cards
    Attributes:
        cards: list of Card Objects
    """
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)

    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return ", ".join(res)

    def size(self):
        return len(self.cards)

    def addCard(self, card):
        """ Add a card to the deck"""
        self.cards.append(card)

    def addMultipleCards(self, cards):
        """ add the multiple cards to existing deck, cards is a list """
        for c in cards:
            self.addCard(c)

    def removeCard(self, card):
        """ remove a card from the deck"""
        self.cards.remove(card)

    def popCard(self, index=0):
        """ removes and returns a card from the deck
        By default removes the last card from the deck
        """
        return self.cards.pop(index)

    def shuffle(self):
        """ shuffle the card deck """
        random.shuffle(self.cards)

    def sort(self):
        """ sorts the card in ascending order """
        self.cards.sort()

    def moveCards(self, hand, num):
        """ Moves the given number of cards from deck to hand
        hand: destination hand object
        num: integer number of cards to move
        """
        for i in range(num):
            hand.addCard(self.popCard())


class Hand(Deck):
    """ Represents a hand of playing cards """
    def __init__(self, label=''):
        self.cards = []
        self.label = label
