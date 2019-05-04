"""
For this exercise, we will keep track of when our friend’s 
birthdays are, and be able to find that information based 
on their name. Create a dictionary (in your file) of names 
and birthdays. When you run your program it should ask the 
user to enter a name, and return the birthday of that 
person back to them.
"""


def createDict():
	return {"Elvis Presley": "1935.01.08", "Barack Obama": "1961.08.04", "Borat": "1971.10.13", "Djengis Khan": "1162"}

def main():
	birthdays = createDict()
	print("Welcome to the birthay dictionary. We currently know the birthdays of:")
	for key in birthdays:
		print(key)
	
	while 1:
		wantToKnow = input("Whos birthday do you want to know: ")
		if wantToKnow not in birthdays:
			print("Sorry  {} is not in the register. Check your spelling or try another name".format(wantToKnow))
			continue

		if wantToKnow in birthdays:
			print("{}'s birthday is {}".format(wantToKnow, birthdays[wantToKnow]))

if __name__ == '__main__':
	main()