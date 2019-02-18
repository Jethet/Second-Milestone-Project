# The Hand class holds the card objects that are dealt from the deck.
# In addition, the Hand class can calculate the values of the cards using
# the value dict as defined. The Hand class can adjust for the Ace (1 or 11).

import random

# Global variables:
suits = ('Spades', 'Hearts', 'Diamonds', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine',
        'Ten', 'Ace', 'King', 'Queen', 'Jack')
values: {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8,
         'Nine':9, 'Ten':10, 'Ace':11, 'King':10, 'Queen':10, 'Jack':10}

playing = True

class Card():

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

# Create method to print card:
    def __str__(self):
        return self.rank + " of " + self.suit


class Deck():

    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()   # 1) grab deck attricute of deck class
        return single_card

class Hand():   # This defines what cards are in the hand of player

    def __init__(self):
        self.cards = [] # start with empty list
        self.value = 0  # start with zero value
        self.aces = 0   # add attribute to keep track of aces

    def add_card(self, card):
        # taking in a card object from the deck, by calling deal()
        # append it to current list of cards that is in Hand()
        # adjust value to the value of the card that is appended
        self.cards.append(card)
        self.value += values[card.rank]


    def adjust_for_ace(self):
        pass

test_deck = Deck()
test_deck.shuffle()
test_player = Hand()        # define player
pulled_card = test_deck.deal()
print(pulled_card)
test_player.add_card(pulled_card)
print(test_player.value)

#
