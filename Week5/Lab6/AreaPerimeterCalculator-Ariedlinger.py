#AreaPerimterCalculator
#Andrew Riedlinger
#February 21st, 2019
#
#User chooses from menu of choices for calculating
#area and perimeter of rectangles and triangles

import Rectangle
import Circle
import math

#Display the menu
def printMenu():
    """Display the Area/Perimeter Menu"""
    print("\t\tMENU")
    print(
    """
    1) Area of a circle
    2) Circumference of a circle
    3) Area of a rectangle
    4) Perimeter of a rectangle
    5) Quit
    """)
    
#Gets an integer from the user, ensuring proper type and in between the optional
#Mins and max
def getIntInRange(message, min = -math.inf, max = math.inf):
    """Get integer input in given range (Inclusive)"""
    userInput = -math.inf

    while userInput < min or userInput > max or userInput == -math.inf:
        try:
            userInput = int(input(message))
            if userInput < min or userInput > max:
                print("Not a valid option")
        except ValueError:
            print("Not a proper number")

    return userInput

#Gets a float from the user, ensuring proper type and in between the optional
#Mins and max
def getFloatInRange(message, min = -math.inf, max = math.inf):
    """Get integer input in given range (Inclusive)"""
    userInput = -math.inf

    while userInput < min or userInput > max or userInput == -math.inf:
        try:
            userInput = float(input(message))
            if userInput < min or userInput > max:
                print("Not a valid option")
        except ValueError:
            print("Not a proper number")

    return userInput

def main():
    userInput = -1

    while userInput != 5:
        printMenu()

        userInput = getIntInRange("Enter your choice: ", 1, 5)

        if userInput == 1:
            radius = getFloatInRange("Enter the circle's radius: ")
            print("The area is", Circle.area(radius))
        elif userInput == 2:
            radius = getFloatInRange("Enter the circle's radius: ")
            print("The circumference is", Circle.circumference(radius))
        elif userInput == 3:
            width = getFloatInRange("Enter the rectangle's width: ")
            length = getFloatInRange("Enter the rectangle's length: ")
            print("The area is", Rectangle.area(width, length))
        elif userInput == 4:
            width = getFloatInRange("Enter the rectangle's width: ")
            length = getFloatInRange("Enter the rectangle's length: ")
            print("The perimeter is", Rectangle.perimeter(width, length))
        else:
            print("Exiting the program...")
        

#Run the code
main()
