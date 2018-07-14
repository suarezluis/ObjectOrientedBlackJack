def PlayHand():
    import deck
    import hand
    prompt = 'H'
    player = hand.hand()
    dealer = hand.hand()

#new deck
    mazo = deck.deck()

#Shuffle new deck
    mazo.shuffle()

#deal two cards to player
    player.hit(mazo)
    player.hit(mazo)
#deal two cards to dealer and only show the first card
    print("\nThe dealer is showing a",dealer.hit(mazo))
    dealer.hit(mazo)
    
#create loop to keep playing if need it
    while prompt == 'H' and not player.bust() and not player.have21():
        print("\nYour hand:\n")
        player.Print()
        print("You have a total of",player.value())
        prompt = input("\nHit (H) or Stand (S): ").upper()
        if prompt == 'H':
            print("\nYou got the",player.hit(mazo))

#Player black jack, stop asking hit or stand
    if player.blackjack():
        print("\nYour hand:\n")
        player.Print()
        print("************")
        print("*Black Jack*")
        print("************")

#Player has 21, stop asking hit or stand
    if player.have21():
        print("\nYour hand:\n")
        player.Print()
        print("You have a total of",player.value())

#Player busted, stop asking hit or stand and return false
    if player.bust():
        print("\nYour hand:\n")
        player.Print()
        print("You have a total of",player.value())
        print("\nYou busted, Dealer wins!")
        return False        

#Dealer keep getting cards until it reaches 17
    while dealer.value() < 17:
        dealer.hit(mazo)
    print("\nDealer's hand:\n")
    dealer.Print()
    print("Dealer has a total of",dealer.value(),"\n")

#Dealer has blackjack wins and return false
    if dealer.blackjack():
        print("Dealer has a Black Jack!")
        print("Dealer wins!")
        return False

#Player has blackjack wins only if dealer doesnt have blackjack
    if player.blackjack():
        print("Blackjack, you win!")
        return True

#dealer is higher or equal than player without bustin, dealer wins
    if player.value() <= dealer.value() and not dealer.bust():
        print("Dealer wins!")
        return False

#player is higher than dealer
    if player.value() > dealer.value():
        print("Player wins!")
        return True
#dealer bust
    if dealer.bust():
        print("Dealer busted, you win!")
        return True
