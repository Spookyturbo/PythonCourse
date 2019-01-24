#Dice Roll
#Programmer: Andrew Riedlinger
#Date: January 24th, 2019
#
#Rolls two dices and prints out the appropriate term for the roll

import random

die1 = 0
die2 = 0

while(True):
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    total = die1 + die2
    print("You rolled a", die1, "and a", die2)
    if(total == 2):
        print("Snake Eyes")
    elif(total == 3):
        print("Ace Caught a Deuce")
    elif(die1 == 2 and die2 == 2):
        print("Little Joe from Kokomo")
    elif(total == 5):
        print("Little Phoebe")
    elif(die1 == 3 and die2 == 3):
        print("Jimmy Hicks from the Sticks")
    elif((die1 == 6 and die2 == 1) or (die1 == 1 and die2 == 6)):
        print("Six Ace")
    elif(die1 == 4 and die2 == 4):
        print("Eighter from Decatur")
    elif(total == 9):
        print("Nina from Pasadena")
    elif(die1 == 5 and die2 == 5):
        print("Puppy Paws")
    elif((die1 == 6 and die2 == 5) or (die1 == 5 and die2 == 6)):
        print("Sixe Five no Jive")
    elif(total == 12):
        print("Boxcars")

    if(input("Hit enter to roll again, type anything to exit the program...")):
        break
    
        
