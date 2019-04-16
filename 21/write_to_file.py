"""
Take the code from excerice 19, (decode_web_page_2.py) and write it to a file instead of printing it to screen
Ask the user to input the name of the file that will be saved
"""

import requests
from bs4 import BeautifulSoup

url = "https://www.theregister.co.uk/2014/08/26/top_ten_gaming_keyboard_and_mouse_combos/"
page_string = "?page="


def printpage(url):
	pagesoup = BeautifulSoup(requests.get(url).text, "html.parser")
	for body in pagesoup.find_all("p"):
		print(body.text)

def printToFile(url, filename):
	pagesoup = BeautifulSoup(requests.get(url).text, "html.parser")
	"""open(filename, "w") will write from the beginning of the file 
	and overwrite any text, use the "a"-mode to append text to the end of the file"""
	open_file = open(filename, "a")
	for body in pagesoup.find_all("p"):
		open_file.write(body.text + "\n")
	open_file.close()



def main():
	soup = BeautifulSoup(requests.get(url).text, "html.parser")
	
	link = soup.find(rel="canonical")
	front_page = link["href"]
	
	filename = input("Save file as:")
	filename = filename + ".txt"

	i = 1
	for i in range (1, 7):
		printToFile(front_page+page_string+str(i), filename)




if __name__ == "__main__":
	main()