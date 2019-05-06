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





def printGameBoard(game):


	hor = " --- --- ---"
	for row in game:
		print(hor)
		for sq in row:
			if sq == 0:
				print("|   ", end="")
			elif sq == 1:
				print("| x ", end="")
			elif sq == 2:
				print("| o ", end="")
		print("|")
	print(hor)



if __name__	== "__main__":
	#gameBoard(int(input("Enter the size of board you want: ")))
	printGameBoard([[1,1,1],
		   			[0,0,1],
		    		[0,2,0]])