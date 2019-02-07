#Sdrawkcab (Backwards)
#Andy Riedlinger
#February 6th, 2019
#
#Takes a message from the user and prints it out backwards

message = input("Enter a message: ")

print("Your message backwards is:", message[::-1])

#Method 2
#str = ""
#for letter in message:
#    str = letter + str

#print(str)

#Method 3
#for i in range(len(message) - 1, -1, -1):
#    print(message[i], end="")

    
