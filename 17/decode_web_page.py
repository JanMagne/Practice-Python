"""
Print a list of all the headlines from The New York Times web page

Use BeatuifulSoup and requests for this.
"""

import requests
from bs4 import BeautifulSoup



if __name__ == '__main__':

	vg = "https://www.vg.no/nyheter/"
	usrinp = str(input("Velkommen til Jannis VG, vil du lese innenriks eller utenriks nyheter?\n"))
	url = vg + usrinp
	print("Henter nyheter fra: " + url + "\n")
	soup = BeautifulSoup(requests.get(url).text,'html.parser')

	nyheter = soup.find_all(class_="_2arR4")

	for _2arR4 in nyheter:
		print(_2arR4.find("h2").text)

