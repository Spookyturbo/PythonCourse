#Match Coins
#Andrew Riedlinger
#March 7th, 2019
#
#A coin toss game with two players

import random

class Coin(object):
    """Virtual coin flipping"""
    def __init__(self, amount = 20):
        self.__amount = amount
        self.__sideup = "Heads"

    def get_amount(self):
        return self.__amount

    def set_amount(self, change):
        self.__amount += change
        if self.__amount < 0:
            self.__amount = 0

    def get_sideup(self):
        return self.__sideup

    def toss(self):
        side = random.randint(0, 1)
        if side == 0:
            self.__sideup = "Heads"
        else:
            self.__sideup = "Tails"

def main():
    player1 = Coin()
    player2 = Coin()
    loops = 0
    #Continue playing if want to continue, and neither players have zeroed out
    play = input("Do you want to continue? ").lower()
    while play == 'y' and player1.get_amount() > 0 and player2.get_amount() > 0:
        player1.toss()
        player2.toss()

        if player1.get_sideup() == player2.get_sideup():
            print("Player 1 Wins!")
            player1.set_amount(1)
            player2.set_amount(-1)
        else:
            print("Player 2 Wins!")
            player2.set_amount(1)
            player1.set_amount(-1)

        print("Player1 tossed a", player1.get_sideup(), "and Player 2 tossed", player2.get_sideup())
        play = input("Do you want to continue? ").lower()

    print("Player1 :", player1.get_amount(), "cents, and Player2 :", player2.get_amount(), "cents.")

main()
input("<ENTER> to quit.")
        
        
        
