"""
Let the user input a string, and tell him if its an palindrome or not
"""


print("Hey! I am gonna tell you if your input text is a palindrome or not")
usrinp = input("Enter the text here: ")
print("You are wondering if '" + usrinp + "' is a palindrome.")

ispal = True
for c in usrinp:
	i = usrinp.index(c)*-1
	if c == usrinp[i]:
		ispal = True
	else:
		ispal = False

if ispal == True:
	print(usrinp + " is a palindrome!")
else:
	print(usrinp + " is not a palindrome..")
	