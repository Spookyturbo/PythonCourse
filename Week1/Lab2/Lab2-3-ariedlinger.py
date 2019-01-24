#Lab2-3-ariedlinger.py
#Tipper Program
#Andrew Riedlinger
#January 19th, 2019

#Ensure it is a positive number entered
billTotal = -1
while(billTotal < 0):
    try:
        billTotal = float(input("What was your bill total? "))
        if(billTotal < 0):
            print("Not a valid number, please try again")
    except ValueError:
        print("Not a valid number, please try again")

smallTip = billTotal * 0.15
largeTip = billTotal * 0.2

print("\n15% Tip:", smallTip)
print("20% Tip:", largeTip)

input("\n\nPress enter to exit...")
