"""
Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, 
then tell them whether they guessed too low, too high, or exactly right.
"""

import random

number = random.randint(1, 10)
userguess = input("Im thinking of a number between 1 and 10, what do you think it is?\n")

tries = 1
while 1:
    
    if userguess == "exit":
        break
    if int(userguess) == number:
    
        if tries == 1:
            print("Are you a wizard!? O_o\nYou win the game on first try!")
            userguess = input("You are so awesome at this game!! I have a new number! try it now: ")
        else:         
            print("Yes my number is "+ str(number) + ". You guessed correctly in " + str(tries) + " tries!")
            userguess = input("You are so awesome at this game!! I have a new number! try it now: ")
        tries = 1
        number = random.randint(1, 10)
        
    elif int(userguess) < number:
        userguess = input("My number is higher, try a new one: ")
        tries += 1
        
    else:
        userguess = input("My number is lower, try a new one: ")
        tries += 1
    