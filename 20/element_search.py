"""
Write a func that takes in an ordered list, and decides if the given number is inside the list.
Do this using binary search in the list
"""
import random
import time


def printList(list):
	""" Just a simple thing to print all elems of a list"""
	print("list has "+str(len(list))+" elements, and they are:")
	for elem in list:
		print(elem, end = ', ')



def binarySearch(list_to_search, x):
	""" Reqursive binary search, using slices """
	mid = int(len(list_to_search)/2)
	if list_to_search[mid] == x:
		print("found match, breaking reqursion..")
		return True
	if len(list_to_search) <= 1:
		print("search done, no match, breaking reqursion..")
		return False


	elif x < list_to_search[mid]:
		print("Search left")
		return binarySearch(list_to_search[:mid], x)
	elif x > list_to_search[mid]:
		print("Search right")
		return binarySearch(list_to_search[mid:], x)




def newlist():
	""" Gives a new sorted list """
	mylist = []
	for x in range (0,6000):
		mylist.append(random.randint(1,1000))
	mylist.sort()

	return mylist


if __name__=="__main__":

	mylist = newlist()

	printList(mylist)

	looking_for = int(input("\nEnter the number you are searching for\n"))

	if binarySearch(mylist, looking_for):
		print(str(looking_for) + " is in the list")

	else:
		print("sorry " + str(looking_for) + " is not in the list")
