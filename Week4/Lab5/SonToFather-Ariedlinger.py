#SonToFather
#Andy Riedlinger
#February 14th, 2019
#
#Finds the father/grandfather of an entered name after
#looking it up in a dictionary

#Ensure a valid int is entered between the min and max values
def getUserNumber(min, max, output):
    value = min - 1
    while value < min or value > max:
        try:
            value = int(input(output))
            if value < min or value > max:
                print("Not a valid option, please try again")
        except ValueError:
            print("Invalid number try again")
            
    return value

sonsToFathers = {"John Quincy Adams" : "John Adams", "Bart Simpson" : "Homer Simpson",
                 "Homer Simpson" : "Grandpa Simpson", "John Adams" : "John Adams Sr.",
                 "Luke Skywalker" : "Anakin Skywalker", "Son of John Quincy Adams" : "John Quincy Adams"}

choice = -1

#Exit once user enters 0
while(choice != 0):
    print(
    """
        Father Finder

        0 - Quit
        1 - Find a Father
        2 - Find a Grandfather
        3 - List Sons
        
    """
    )

    choice = getUserNumber(0, 3, "Choice: ")

    if choice == 0: #Quit
        print("So long.")
    elif choice == 1: #Find a father
        son = input("Enter the son: ").title()
        if son in sonsToFathers:
            print("His father is", sonsToFathers[son])
        else:
            print("His father is unknown")
    elif choice == 2: #Find a grandfather
        grandson = input("Enter the grandson: ").title()
        if grandson in sonsToFathers:
            father = sonsToFathers[grandson]
            if father in sonsToFathers:
                print("His grandfather is", sonsToFathers[father])
            else:
                print("His grandfather is unknown")
        else:
            print("His grandfather is unknown")
    elif choice == 3: #List sons
        print(sonsToFathers.keys())

