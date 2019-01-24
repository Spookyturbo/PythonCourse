#Guess My Number
#Andrew Riedlinger
#January 24th, 2019
#
#The computer picks a random number between 1 and 100
#The player tries to guess it and the computer lets
#the player know if the guess is too high, too low
#or right on the money

import random

print("\tWelcome to 'Guess My Number'!")
print("\nI'm thinking of a number between 1 and 100.")
print("Try to guess it in as few attempts as possible.\n")

#set the initial values
theNumber = random.randint(1, 100)
guess = int(input("Take a guess: "))
tries = 1

#guessing loop
while(guess != theNumber):
    if(guess > theNumber):
        print("Lower...")
    else:
        print("Higher...")

    guess = int(input("Take a guess: "))
    tries += 1

#Congratulations
print("You guessd it! The number was", theNumber)
print("And it only took you", tries, "tries!\n")

input("\n\nPress the enter key to exit.")
