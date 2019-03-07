#Games
#Andrew Riedlinger
#March 7th, 2019
#
#Demonstrates module creation (And used in blackjack program)

class Player(object):
    """A player for a game."""
    def __init__(self, name, score = 0):
        self.name = name
        self.score = score

    def __str__(self):
        rep = self.name + ":\t" + str(selfs.score)
        return rep

def ask_yes_no(question):
    """Ask a yes or no question."""
    response = None
    while response not in ("y", "n"):
        response = input(question).lower()
    return response

#High is exclusive
def ask_number(question, low, high):
    """Ask for a number within a range."""
    response = None
    while response not in range(low, high):
        try:
            response = int(input(question))
        except ValueError:
            print("Not an integer")
    return response

if __name__ == "__main__":
    print("You ran this module directly  (and did not 'import' it).")
    input("\n\nPress the enter key to exit.")
