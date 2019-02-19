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



#
