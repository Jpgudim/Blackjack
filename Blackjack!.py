import random

Ace = 11
Jack = 10
Queen = 10
King = 10

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

player_card1 = random.choice(deck)
deck.remove(player_card1)
dealer_card1 = random.choice(deck)
deck.remove(dealer_card1)
player_card2 = random.choice(deck)
deck.remove(player_card2)
dealer_card2 = random.choice(deck)
deck.remove(dealer_card2)

def get_score(who):
    if who == "player":
        score = int(player_card1) + int(player_card2)
    if who == "dealer":
        score = int(dealer_card1) + int(dealer_card2)
    return score




start = input("Welcome to blackjack! Press enter to start.")
print ()

print ("Your first card: " + str(player_card1))
print ("The dealer's first card: " + str(dealer_card1))
print ("Your second card: " + str(player_card2))
print ("The dealer has been delt a second card, but it's face down!")
print ()

print (player_card1)
print (player_card2)
print (dealer_card1)
print (dealer_card2)
print ()
print(get_score("player"))
print(get_score("dealer"))
print ()
print (deck)






