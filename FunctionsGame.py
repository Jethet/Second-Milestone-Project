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
