#DealEm
#Andy Riedlinger
#February 7th, 2019
#
#Deals hands of cards to players from a deck (Duplicates allowed)

import random

#Gurantee proper numbers are inputed
def getNumber(output):
    number = -1
    while number < 0:
        try:
            number = int(input(output))
            if number < 0:
                print("Not a valid number, try again")
        except ValueError:
            print("Not a valid number, try again")

    return number


SUITS = ('c', 'h', 's', 'd')
CARDVALUES = ('A', '2', '3', '4','5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')

#Initialization for loop
players = 53
handSize = 1

#Ensure there are enough cards for specified players and hands
while players * handSize > 52:
    players = getNumber("How many people will be playing? ")
    handSize = getNumber("How many cards should be in each players hand? ")

    if players * handSize > 52:
        print("\nThere are not enough cards for this many players\n")

#Create the deck
deck = ()
for suit in SUITS:
    for cardValue in CARDVALUES:
        deck += (cardValue + suit,)

hands = []

#Create all the hands and store in the hands list
for playerNumber in range(players):
    hand = ()
    for cardNumber in range(handSize):
        deckPosition = random.randrange(len(deck))
        hand += (deck[deckPosition],)
        deck = deck[:deckPosition] + deck[deckPosition + 1:]

    hands.append(hand)

#Print out the hands
for hand in hands:
    print("\n")
    print(hand)
    
input("\n\nPress enter to exit...")

