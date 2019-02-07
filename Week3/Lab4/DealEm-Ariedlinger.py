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

players = getNumber("How many people will be playing? ")
handSize = getNumber("How many cards should be in each players hand? ")

SUITS = ('c', 'h', 's', 'd')
CARDVALUES = ('A', '2', '3', '4','5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')

hands = []

#Create all the hands and store in the hands list
for playerNumber in range(players):
    hand = ()
    for cardNumber in range(handSize):
        cardValue = random.choice(CARDVALUES)
        suit = random.choice(SUITS)
        hand += (cardValue + suit,)

    hands.append(hand)

#Print out the hands
for hand in hands:
    print("\n")
    print(hand)
  
        
input("\n\nPress enter to exit...")
