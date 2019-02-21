#Check Digit Calculator
#Andrew Riedlinger
#February 21st, 2019
#
#With a given UPC calculate the check digit for UPC-A
#and determine if the label is valid

#Expects upc as a string

CHECK_DIGIT_POSITION = 12

#Gets a UPC of correct length, type, and non negative from the user
def askForUPC(message):
    """Gets a valid upc candidate from user"""
    validUPC = False
    upc = None

    while not validUPC:
        upc = input(message)
        #len must be 12 for upc-a
        if len(upc) != 12:
            print("Incorrect length")
        else:
            #Check to see if valid number
            try:
                #Keep UPC as string, otherwise 0s on front will be cut off
                numberTest = int(upc)
                if numberTest < 0:
                    print("UPC can't be negative")
                else:
                    validUPC = True
            except ValueError:
                print("Not an integer number")

    return upc

#Finds the checkDigit for given UPC
#Input should be a string
def Find_UPC(upc):
    """Finds the check digit for given upc"""
    upc = str(upc)

    if len(upc) != 12:
        print("Invalid UPC given")
        return None

    checkDigit = 0
    
    for digit in range(0, len(upc) - 1):
        if (digit + 1) % 2 == 0:
            checkDigit += int(upc[digit])
        else:
            checkDigit += 3 * int(upc[digit])
    checkDigit %= 10

    if checkDigit != 0:
        checkDigit = 10 - checkDigit

    return checkDigit

#Checks the check digit given against the UPC to see if valid
def isUpcValid(upc, checkDigit):
    """checks if given check digit is in the given upc"""
    upc = str(upc)
    return checkDigit == int(upc[CHECK_DIGIT_POSITION - 1])

#Main run
def main():
    #retrieve the UPC, CheckDigit, and check it
    upc = askForUPC("Enter a product labels UPC: ")
    checkDigit = Find_UPC(upc)
    
    if(isUpcValid(upc, checkDigit)):
        print("UPC is valid!")
    else:
        print("UPC is invalid!")
        
    input("\n\nPress enter to exit...")

#Run code
main()
    
