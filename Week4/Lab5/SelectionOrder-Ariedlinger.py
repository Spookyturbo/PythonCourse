#SelectionSort
#Andy Riedlinger
#February 14th, 2019
#
#This takes a list from 0-9 and sorts it in ascending order
#without using the sort method python supplies

import random

unordered = list(range(0,10))
ordered = []
random.shuffle(unordered)

print("Unordered list:\n", unordered)

#Sorting
while unordered:
    lowest = unordered[0]
    for number in unordered:
        
        if number < lowest:
            lowest = number
    #Sort that element in the list
    ordered.append(lowest)
    unordered.remove(lowest)

    #Display progress
    #print("Unordered:", unordered)
    #print("Ordered", ordered)

print("Ordered list:\n", ordered)

input("\n\nPress enter to exit...")

