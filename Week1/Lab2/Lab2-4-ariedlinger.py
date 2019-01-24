#Lab2-4-ariedlinger.py
#Car Salesman Program
#Andrew Riedlinger
#January 19th, 2019

#Used to ensure inputs are non negative real floats
def getFloatInput(output):
    value = -1
    while(value < 0):
        try:
            value = float(input(output))
            if(value < 0):
                print("Not a valid number, please try again")
        except ValueError:
            print("Not a valid number, please try again")

    return value

#Changing to float to allow cents
carPrice = getFloatInput("What is the base price of the car? ")
taxPercent = 6.25
licensePercent = 5

#If the user enters the values uncomment this, it was unclear what they book wanted
#taxPercent = getFloatInput("What is the tax rate in percent? ")
#licensePercent = getFloatInput("What is the license rate in percent? ")

taxCost = carPrice * (taxPercent / 100)
licenseCost = carPrice * (licensePercent / 100)

dealerPrep = 200
destinationCharge = 500

#If the user enters the values uncomment this
#dealerPrep = getFloatInput("What is the dealer preparation cost? ")
#destinationCharge = getFloatInput("What is the destination charge? ")

totalCarPrice = carPrice + taxCost + licenseCost + dealerPrep + destinationCharge


print("\nThe total price of the car after tax, license, prep, and destination charges is $", "{:.2f}".format(totalCarPrice))

input("\n\nPress enter to exit...")
