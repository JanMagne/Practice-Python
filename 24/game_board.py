"""
Draw a game board, like for chess or tic-tac-toe. Ask the user what size he wants
 --- --- --- 
|   |   |   | 
 --- --- ---  
|   | o |   | 
 --- --- ---  
|   |   | x | 
 --- --- --- 
"""





def printGameBoard(scale):

	ver = "|   "*(scale + 1)
	hor = " ---"*scale

	for i in range(scale*2):
		if i % 2 == 0:
			print(hor)
		else:
			print(ver)

	print(hor)



if __name__	== "__main__":
	#gameBoard(int(input("Enter the size of board you want: ")))
	printGameBoard(3)