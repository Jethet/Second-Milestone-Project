# This is the code logic for the blackjack game.

while True:
    # opening statement:
    print("Welcome to Blackjack!")
    # create deck, shuffle deck:
    deck = Deck()
    deck.shuffle()
    # deal two (2) cards to player:
    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())
    # deal two (2) cards to dealer:
    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    # set up player's chips:
    player_chips = Chips()
    # prompt player for bet:
    take_bet(player_chips)
    # show cards (at start of the game, one dealer card hidden):
    show_some(player_hand,dealer_hand)

    while playing:
        # prompt player to hit or stand:
        hit_or_stand(deck,player_hand)
        # show cards (keep one dealer card hidden):
        show_some(player_hand,dealer_hand)
        # if player's hand > 21, run player_busts() and break out of loop:
        if player_hand.value > 21:
            player_busts(player_hand,dealer_hand,player_chips)
            break
    # if player has not busted, play dealer's hand until dealer has 17:
    if player_hand.value <= 21:
        while dealer_hand.value < 17:
            hit(deck,dealer_hand)
        # dealer is playing so all cards should be visible:
        show_all(player_hand,dealer_hand)

        # run different scenarios for winning:
        if dealer_hand.value > 21:
            dealer_busts(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand,dealer_hand,player_chips)
        else:
            push(player_hand,dealer_hand)

    # inform player of their chips total:
    print('\nPlayer total chips are at: {}'.format(player_chips.total))
    # ask player if they want to play again:
    new_game = input("Would you like to play again? y/n")
    if new_game[0].lower() == 'y':
        playing = True
        continue
    else:
        print("Thank you for playing.")
        break

    #
