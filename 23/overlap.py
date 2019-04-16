"""
Take two text files, find the numbers that are overlapping in both files
"""



def listFromFile(filename):
	retList = []
	with open(filename, "r") as f:
		line = f.readline()
		while line:
			retList.append(int(line))
			line = f.readline()

	return retList

def findOverlaps(list1, list2):
	return [elem for elem in list1 if elem in list2]

def main():
	
	primes = listFromFile("primenumbers.txt")
	happy = listFromFile("happynumbers.txt")
	overlap = findOverlaps(primes, happy)

	for elem in overlap:
		print(elem)

if __name__ == "__main__":
	main()