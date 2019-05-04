"""
Use the 'bokeh' library to plot the histogram of months from the birthdays.json

"""

import json
from collections import Counter
from bokeh.plotting import figure, show, output_file

def main():
	output_file("plot.html")


	with open("birthdays.json", "r") as f:
		birthdays = json.load(f)
	
	months = []

	for x in birthdays.values():
		months.append(x.split(".")[1])

	months = [int(x) for x in months]
				
	count = Counter(months)
	month_list = list(count.values())
	month_nums = list(count.keys())


	p = figure(title="Jannis")

	p.vbar(x=month_nums, top=month_list, width=0.5)

	show(p)

if __name__ == '__main__':
	main()