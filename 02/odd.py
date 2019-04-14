# The user inputs a number, tell him wheter its an odd or even number
# Extra 1: Tell him if the number is divisible by 4
# Extra 2: Make the user insert two numbers and tell him if the first one is divisible by the second

num = int(input ("Which number are you wondering about? "))

if  num % 4 == 0 and num % 2 == 0:
	print (str(num) + " is an even number and is divisible by FOOOOUR!")

elif num % 2 == 0:
	print (str(num) + " is an even number!!!!")
	
else:
	print (str(num) + " is an odd number")
	
print ("Now.. You wanna know if x is divisible by y?")
x = int(input("Enter x:"))
y = int(input("Enter y:"))

if x % y == 0:
	print(str(x) + " is divisible by " + str(y) + " !! :)")

else:
	print(str(x) + " is not divisible by " + str(y) + " the remainder is " + str(x%y))
 