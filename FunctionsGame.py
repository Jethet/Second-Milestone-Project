# The functions to be used to play the blackjack game:

def take_bet(chips):

    while True:
        try:
            chips.bet = int(input("How many chips do you want to bet? "))
        except:
            print("Sorry, please provide an integer.")
        else:
            if chips.bet > chips.total:
                print("Sorry, you do not have enough chips. \
                You have {}".format(chips.total))
            else:
                break

def hit(deck, hand):
    single_card = deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_ace()

def hit_or_stand(deck,hand):
    global playing   # to control the upcoming while loop
    while True:
        x = input("Hit or stand? Enter h or s. ")
        if x[0].lower() == 'h':
            hit(deck,hand)
        elif x[0].lower() == 's':
            print("Player Stands. Dealer's turn.")
            playing = False

        else:
            print("Please enter h or s only.")
            continue
        break

# The following are functions to handle END OF GAME scenarios:
# parameters are player's hand, dealer's hand and chips.

def player_busts(player,dealer,chips):
    print("Bust player!")
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print("Player wins!")
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print("Dealer busted. Player wins!")
    chips.win_bet()

def dealer_wins(player,dealer,chips):
    print("Dealer wins!")
    chips.lose_bet()

def push(player,dealer):
    print('Dealer and player tie! PUSH!')



#
