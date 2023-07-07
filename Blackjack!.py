import random

# giving score values
Ace = 11
Jack = 10
Queen = 10
King = 10

# this is the card deck
deck = [Ace,Ace,Ace,Ace,
"2", "2", "2", "2",
"3","3","3","3",
"4","4","4","4",
"5","5","5","5",
"6","6","6","6",
"7","7","7","7",
"8","8","8","8",
"9","9","9","9",
"10","10","10","10",
Jack,Jack,Jack,Jack,
Queen,Queen,Queen,Queen,
King,King,King,King,]

# drawing cards for the first turn
player_card1 = random.choice(deck)
deck.remove(player_card1)
dealer_card1 = random.choice(deck)
deck.remove(dealer_card1)
player_card2 = random.choice(deck)
deck.remove(player_card2)
dealer_card2 = random.choice(deck)
deck.remove(dealer_card2)

# function to get the score of the first turn
def get_score(who):
    if who == "player":
        score = int(player_card1) + int(player_card2)
    if who == "dealer":
        score = int(dealer_card1) + int(dealer_card2)
    return score

# initializing player and dealer scores
dealer_score = 0
player_score = 0

# function to play out the dealers turn
def dealer_turn():
    dealer_score = int(get_score("dealer"))
    while dealer_score < 17:
        print ("The dealer is going...")
        dealer_score += int(random.choice(deck))
        print ("The dealer has a score of " + str(dealer_score))
        if dealer_score > 21:
            print ("The dealer busts! You win!")
        if dealer_score == 21:
            print ("The dealer has 21. They win!")
    return dealer_score


start = input("Welcome to blackjack! Press enter to start.")
print ()
print ("Your first card: " + str(player_card1))
print ("The dealer's first card: " + str(dealer_card1))
print ("Your second card: " + str(player_card2))
print ("The dealer has been dealt a second card, but it's face down!")
print ()
print ("Your score: " + str(get_score("player")))
print ("The dealer's current score: " + str(dealer_card1))

player_score = get_score("player")

if player_score == 21:
    print ("You have 21! You win!")
else:
    turn = input("Your turn! What would you like to do? (type hit or stand) ")
    print()

if turn == "stand":
    print ("The dealer's second card is a " + str(dealer_card2))
    print ("The dealer has a score of " + str(get_score("dealer")))
    dealer_score = dealer_turn()
elif turn == "hit":
    decision = "hit"
    while decision == "hit":
        print ("The dealer gives you a card...")
        player_score = get_score("player")
        player_score += int(random.choice(deck))
        print ("Your score is now " + str(player_score))
        if player_score > 21:
            print ("You went over 21! You lose")
            print ("The dealer's second card was a " + str(dealer_card2))
            print ("The dealer had a score of " + str(get_score("dealer")))
            break
        else:
            decision = input("What would you like to do? (type hit or stand) ")
        if decision == "stand":
            dealer_score = dealer_turn()
            break

player_score = int(player_score)
dealer_score = int(dealer_score)

if player_score < 21 and dealer_score < 21:
    if player_score > dealer_score:
        print ("You have a score of %s, and the dealer has a score of %s" % (player_score, dealer_score))
        print (" You have the higher score. You win!")
    if dealer_score > player_score:
        print ("You have a score of %s, and the dealer has a score of %s" % (player_score, dealer_score))
        print (" The dealer has the higher score. The house wins!")


        






