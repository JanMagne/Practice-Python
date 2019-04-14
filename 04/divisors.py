"""
Create a program that asks the user for a number and then prints out a list of all the divisors of that number. 
"""


number = int(input("Enter the number you want to know the dividers of"))
candidates = range(1, number+1)
divisors = []

for x in candidates:
	if number % x == 0:
		divisors.append(x)
		
print (divisors)
	