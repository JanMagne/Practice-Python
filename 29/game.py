"""
Combine the previous three tasks to create a full Tic-Tac-Toe game in the terminal
"""
from CheckWinner import *
from GameBoard import *
from UserInput import *



def getNewGame():
	return [[0,0,0],
		    [0,0,0],
		    [0,0,0]]

def welcome():
	print("Welcome to Tic-Tac-Toe")
	print("You are gonna be asked to input the coordinates for your square")
	print("Please enter them as coordinates like (x,y) from 1 to 3")
	print("Player 1 plays as 'x', player to plays as 'o'")
	print("Here we go:\n")
	printGameBoard(getNewGame())

def main():
	welcome()
	game = getNewGame()
	whosTurn = 1
	
	while 1:
		game = usrinp(game, whosTurn)
		printGameBoard(game)

		if checkForWinner(game):
			print("The winner is " + checkForWinner(game))
			break

		if whosTurn == 1:
			whosTurn = 2
		elif whosTurn == 2:
			whosTurn = 1


	print("Thanks for playing. Please come again! \n- Jannis, 2019")
if __name__ == '__main__':
	main()