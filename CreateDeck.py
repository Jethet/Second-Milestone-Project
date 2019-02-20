import random

# Global variables:
suits = ('Spades', 'Hearts', 'Diamonds', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine',
        'Ten', 'Ace', 'King', 'Queen', 'Jack')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8,
         'Nine':9, 'Ten':10, 'Ace':11, 'King':10, 'Queen':10, 'Jack':10}

playing = True

# Create class cards with attributes suit, rank

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

    # This method prints the deck:
    def __str__(self):
        deck_comp = ''      # Empty string for total deck composition
        for card in self.deck:
            deck_comp += '\n' + card.__str__()
        return "The deck has: "+deck_comp

    # This method does not return anything but shuffles the deck in place
    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()   # 1) grab deck attribute of deck class
        return single_card              # 2) pop off a card item from that list
                                        # 3) set that to single_card and return


# This runs OK and prints the entire deck, shuffled.
#test_deck = Deck()
#test_deck.shuffle()
#print(test_deck)

# CREATE HAND code

class Hand:

    def __init__(self):
        self.cards =[]   # start with an empty list
        self.value = 0   # start with zero value
        self.aces = 0    # at an attribute to keep track of aces

    def add_card(self, card):
        # card is passed in from Deck.deal() ---> single Card(suit,rank)
        self.cards.append(card)
        self.value += values[card.rank]

        # Track aces:
        if card.rank == 'Ace':
            self.aces += 1


    def adjust_for_ace(self):
        # If total value IN HAND > 21 and still ace in hand of player:
        # then change Ace to be 1 instead of 11:
        while self.value > 21 and self.aces: > 0  # 0 = False, over 0 = True
            self.value -= 10
            self.aces -= 1


class Chips():

    def __init__(self):
        self.total = 100
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet



# Test that value of card is added to player's value:
test_deck = Deck()
test_deck.shuffle()
# create player:
test_player = Hand()
# deal 1 card from deck: CARD(suit,rank)
test_player.add_card(test_deck.deal())
print(test_player.value)



#
