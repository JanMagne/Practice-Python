"""Take a list and write a program that prints out all the elements of the list that are less than 5.

Extras:
Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list.
Write this in one line of Python.
Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user.
"""
import random


li = []
li2 = []
x = 0

while x < 100:
	li.append(random.randrange(1,10000))
	x = x+1
print(li)

lessthan = int(input("Whats your max? "))
for x in li:
	if x < lessthan:
		li2.append(x)

print (li2)
