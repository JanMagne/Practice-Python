"""
In the previous exercise we created a dictionary of famous scientists’ birthdays. In this
exercise, modify your program from Part 1 to load the birthday dictionary from a JSON file on
disk, rather than having the dictionary defined in the program.
"""

import json




def main():

	with open("birthdays.json", "r") as f:
		birthdays = json.load(f)
	print(birthdays)


if __name__ == '__main__':
	main()