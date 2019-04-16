"""
Using requests and beautifulSoup, write a program to write the text of a long web article.
If the article is in several pages, write all of them to the screen

"""

import requests
from bs4 import BeautifulSoup

url = "https://www.theregister.co.uk/2014/08/26/top_ten_gaming_keyboard_and_mouse_combos/"
page_string = "?page="


def printpage(url):
	pagesoup = BeautifulSoup(requests.get(url).text, "html.parser")
	for body in pagesoup.find_all("p"):
		print(body.text)


if __name__=='__main__':

	
	soup = BeautifulSoup(requests.get(url).text, "html.parser")
	
	link = soup.find(rel="canonical")
	front_page = link["href"]
	
	i = 1

	for i in range (1, 7):
		printpage(front_page+page_string+str(i))

