#Word Frequency
#Andrew Riedlinger
#February 28th, 2019
#
#Count the frequency with which each word appears in text

import sys

def getInput(msg):
    value = ''
    while value not in ('y', 'n'):
        value = input(msg).lower()

    return value

def wordFreq(file):
    """Find the frequency of all words in file"""
    freq = {}

    line = file.readline()
    punctChars = ('!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '=', '_', '+', '`', '~', '\'', '"', ';', ':', '[', '{', ']', '}', '/', '?', '.', '>', ',', '<', '|', '\\')

    #Run for all lines of file
    while line:
        #Remove punctuation
        for c in punctChars:
            line = line.replace(c, "")

        words = line.split()

        for word in words:
            tmp = word.lower()
            #Add word key to dicitionary/add 1 to value for key
            freq[tmp] = freq.get(tmp, 0) + 1

        line = file.readline()

    return freq

        

def printOut(data):
    """Print out dictionary organized"""
    for word in sorted(data.keys()):
        print("\t\t", word, " :: ", data[word])

def main():
    """Main loop"""
    end = 'n'

    while end == 'n':
        filename = input("What file do you want to process? ")
        try:
            file = open(filename, "r")
        except IOError:
            print("There was an error opening that file")
        else:
            freqWd = wordFreq(file)

            printOut(freqWd)

        end = getInput("Do you want to exit the program? (y|n)")

    #If the file wasn't created to being with, can't be closed
    try:
        file.close()
    except UnboundLocalError:
        pass

main()
