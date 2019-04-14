"""
Create a program that plays the Cows and Bulls game with the user

The game is like this:
A random 4-digit number is made, and the user needs to guess it.
A correct guessed digit in the correct place is a COW
A correct guessed digit in an incorrect place is a BULL
"""

import random
import time


def cow_bull(number, guess):
	COW = 0
	BULL = 0
	for i in range(len(number)):
		if number[i] == guess[i]:
			COW = COW + 1
		else:
			for j in range(len(number)): #This is not how to Python, should use: guess[i] in number
				if guess[j] == number[i]:
					BULL = BULL + 1
	print("You currently have " + str(COW) + " cows and "+ str(BULL)+" bulls")
	
	if COW != 4:
		new_guess = input("What is your new guess?")
		cow_bull(number, new_guess)
	else:
		return guess





if __name__== '__main__':
	number = str(random.randint(1000, 9999))
	print("I wanna play a game!")
	print("I think of a 4-digit number, try and guess it")
	print("A correct digit on the correct spot gives you a COW")
	print("A correct digit on the Wrong spot gives you a BULL")
	print("Try and get 4 COWS\n")

	first_guess = input("What is your first guess?\n")
	print ("CONGRATULATIONS! You WON the game with the number " + str(cow_bull(number, first_guess)))
	time.sleep(4)

