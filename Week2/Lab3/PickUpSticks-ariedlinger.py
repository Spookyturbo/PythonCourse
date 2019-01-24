#Pick Up Sticks
#Programmer: Andrew Riedlinger
#Date: January 24th, 2019

#Ensure user enters an actual number within a certain range
def getStickInput(output, minValue, maxValue):
    value = -1;
    while(value < minValue or value > maxValue):
        try:
            value = int(input(output))
            if(value > maxValue or value < minValue):
                print("Value must be between", minValue, "and", maxValue)
        except ValueError:
            print("Not a valid integer, please try again.")
    return value
        

maxSticks = 4
minSticks = 1
totalSticks = 13
player = 0

#Instructions
print("\t\tWelcome to Pick Up Sticks.\n")
print("Each player takes turns picking up from 1")
print("to 4 sticks from a pile of 13 sticks.")
print("Whoever picks up the last stick wins.")
print("However, you can't take more sticks then there currently are.")
print("To win you must take/guess the remaining number of sticks!\n")

#Game loop
while(totalSticks > 0):
    print("\nPlayer {}".format(player + 1))
    numberOfSticks = getStickInput("- how many sticks will you take? ".format(player + 1), minSticks, maxSticks)

    #Ensures the last player must take the exact amount of sticks
    if(not totalSticks - numberOfSticks < 0):
        totalSticks -= numberOfSticks

    if(totalSticks <= 0):
        print("Player {} wins!".format(player + 1))
    #Change current player to the other player
    player = not player

input("\n\nPress enter to exit")
    
    
    
