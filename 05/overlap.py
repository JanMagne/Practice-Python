"""
Take two lists and return a list than contains only the elements that are common between the lists.
Extra 1: Randomly generate two lists to test this
"""
import random



def generateRandomList():
	
	i = 0
	l = []
	while i < random.randint(4, 20):
		l.append(random.randint(1,30))
		i = i + 1
	return l


a = generateRandomList()
b = generateRandomList()
common = []

a = sorted(set(a))
b = sorted(set(b))
""" Note! The above lines gives lists. A set cant be sorted because the point of a set is that it is not ordered.
	The set {1, 2, 3} is the same as the set {2, 3 , 1} """


print ("List A = " + str(a))
print ("List B = " + str(b))

for elem in a:
	if  elem in b:
		common.append(elem)
		
print("Common elements between these two lists are: " + str(common))
	

