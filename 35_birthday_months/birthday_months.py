"""
Use the previous excersise and the birthdays.json file to extract the months of all birthdays.
Then count how many have a birthday each month.
"""
from collections import Counter
import json


def main():
	with open("birthdays.json", "r") as f:
		birthdays = json.load(f)
	dates = []
	months = []

	for x in birthdays.values():
		dates.append(x)

	for date in dates:
		months.append(date.split(".")[1])
	
	months = [int(x) for x in months]
	
	
	count = Counter(months)

	print(count)

if __name__ == '__main__':
	main()
