# Create a program that asks the user to enter their name and their age. 
# Print out a message addressed to them that tells them the year that they will turn 100 years old.

#Extra 1: Make the user choose how many times to show the message
#Extra 2: Get the current year from datetime.
import datetime


this_year = datetime.datetime.now().year
name = input("Enter your name ")
age = int(input("How old are you? "))
wannabe = int(input("How old do you want to become? "))
year = int((this_year - age) + wannabe)
print ("you are gonna be " + str(wannabe) +" " +"in the year of" + " " +str(year))


i = input("how many times you wanna see that? ")
i = int(i)
for x in range(0, i):
    print ("you are gonna be " + str(wannabe) +" " +"in the year of" + " " +str(year))
