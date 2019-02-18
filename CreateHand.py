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

class Hand():

    def __init__(self):
        self.cards = [] # start with empty list
        self.value = 0  # start with zero value
        self.aces = 0   # add attribute to keep track of aces

    def add_card(self, card):
        pass


    def adjust_for_ace(self):
        pass
