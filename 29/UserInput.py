"""
Take user input to the tic-tac-toe game.
Have the user input their move as and index (col,rov) and put this in the game matrix.
Nb! The user will probably start counting from 1!
"""
from GameBoard import *
from CheckWinner import *


def getNewGame():
	return [[0,0,0],
		    [0,0,0],
		    [0,0,0]]

def welcome(game):
	print("Welcome to Tic-Tac-Toe")
	print("You are gonna be asked to input the coordinates for your square")
	print("Please enter them as coordinates like (x,y) from 1 to 3")
	print("Player 1 plays as 'x', player to plays as 'o'")
	print("Here we go:\n")
	printGameBoard(game)

def printmatrix(matrix):
	for i in range(len(matrix)):
		print(matrix[i])
	print('\n')

def instertToMatrix(game, userid, xy):

	x = int(xy['x'])-1
	y = int(xy['y'])-1


	if userid == 1:
		if game[x][y] == 0:
			game[x][y] = 1
		else:
			print("this position is already taken")
			exit()
	elif userid == 2:
		if game[x][y] == 0:
			game[x][y] = 2
		else:
			print("this position is already taken")
			exit()
	return game

def playerInput(inputstring):
	userinlst = inputstring.split(",")
	coordinates = {'x':0 , 'y':0 }
	coordinates['x'] = userinlst[0].strip()
	coordinates['y'] = userinlst[1].strip()
	return coordinates

def winMsg(winner):
	print("Gongratz! " + winner+ " is the winner!")
	exit()

def welcome(game):
	print("Welcome to Tic-Tac-Toe")
	print("You are gonna be asked to input the coordinates for your square")
	print("Please enter them as coordinates like (x,y) from 1 to 3")
	print("Player 1 plays as 'x', player to plays as 'o'")
	print("Here we go:\n")
	printGameBoard(game)

def usrinp(game, playerID=1):
	welcome(game)
	while 1:
		coordinates = playerInput(input("PLayer One, Enter your coordinates as x, y "))
		instertToMatrix(game, 1, coordinates)
		printGameBoard(game)
		winner = checkForWinner(game)
		if winner:
			winMsg(winner)

		coordinates = playerInput(input("PLayer Two, Enter your coordinates as x, y "))
		instertToMatrix(game, 2, coordinates)
		printGameBoard(game)
		checkForWinner(game)
		winner = checkForWinner(game)
		if winner:
			winMsg(winner)



if __name__ == "__main__":
	game = getNewGame()
	usrinp(game)