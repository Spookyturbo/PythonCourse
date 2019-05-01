#Alien Blaster
#Andrew Riedlinger
#March 22nd, 2019
#
#Have a hero and an alien blast each other

import random

class Player:
    """A base player class"""

    def blast(self, enemy):
        enemy.die()

    def die(self):
        print('Player died')

class Hero(Player):

    def __init__(self, name = 'Arnold'):
        self.name = name
        self.health = 10
        self.shield = 10
        self.life = 1

    def die(self):
        self.health -= 4
        if self.health <= 0:
            self.life -= 1

        if self.life <= 0:
            print("We will now give silence for a few seconds for our friend, Joe.")
        else:
            print("You just nicked me.")

class Alien(Player):

    def __init__(self, name = 'Zxblrb'):
        self.name = name
        self.health = 10
        self.shield = 10
        self.life = 1

    def die(self):
        self.health -= 4

        if self.health <= 0:
            self.life -= 1

        if self.life <= 0:
            print("The alien gasps and says, 'Oh, this is it. This is the big one.")
            print("Yes, it's getting dark now. Tell my 1.6 million larvae that I loved them...")
            print("Good-bye, cruel universe.")
            print("...we will now give silence for a few seconds for each larvae to say a few words for", self.name, ".")
            print("Wklsdf fdocmvowz foew.\n"*3)
            print("Ok, shut up!")
        else:
            print("You can't even hit a schlurg")

def main():
    hero = Hero()
    alien = Alien()

    while(alien.health > 0 and hero.health > 0):
        if(random.randint(0, 1) == 0):
            print("The hero blasts an enemy.")
            hero.blast(alien)
        else:
            print("The alien blasts the player.")
            alien.blast(hero)

    print("\nGame over")

main()
input("\n\nPress the enter key to exit.")
