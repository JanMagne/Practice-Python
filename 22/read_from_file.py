"""
Given a .txt file with a bunch of names, count how many times each name appears in the file
"""
def printList(list):
	""" Just a simple thing to print all elems of a list"""
	print("list has "+str(len(list))+" elements, and they are:")
	for elem in list:
		print(elem, end = ', ')


def listFromFile(filename):
		
	names_in_file = []
	with open(filename, "r") as open_file:
		for line in open_file:
			filetext = open_file.readline()
			names_in_file.append(filetext.strip())

	return names_in_file


def main():
	filename = "names.txt"

	counter = {}
	names = listFromFile(filename)

	for name in names:
		if name in counter:
			counter[name] += 1
		else:
			counter[name] = 1
	print(counter)

if __name__ == "__main__":
	main()