#Useless Trivia
#Andrew Riedlinger
#January 19th, 2019

name = input("Hi, What's your name? ")

age = input("How old are you? ")
age = int(age)

weight = int(input("Okay, last question. How many pounds do you weigh? "))


print("\nIf poet ee cummings were to email you, he'd address you as", name.lower())
print("But if ee were mad, he'd call you", name.upper())

called = name * 5


print("\nIf a small child were trying to get your attention")
print("your name would become:")
print(called)

seconds = age * 365 * 24 * 60 * 60
print("\nYou're over", seconds, "seconds old.")

moonWeight = weight / 6
print("\nDid you know that on the moon you would weigh only", moonWeight, "pounds?")

sunWeight = weight * 27.1
print("On the sun, you'd weigh", sunWeight, "(but, ah... not for long).")

input("\n\nPress the enter key to exit.")
