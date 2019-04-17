"""
If a game of Tic Tac Toe is represented as a list of lists, like so:

game = [[1, 2, 0],
		[2, 1, 0],
		[2, 1, 1]]

Given this list, tell me if one of the players has won.
"""
game = [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 0]]

def checkRows(game):
	for rows in game:
		if rows.count(1) == 3:
			return "player_one"
		if rows.count(2) == 3:
			return "player_two"
	return 0


def checkColumns(game):
# """Rotate the game matrix and use checkRows to check the columns"""

# 	# The following loops is how i would rotate the matrix
# 	columns = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
# 	i = 0
# 	j = 0
# 	for rows in game:
# 		for square in rows:
# 			columns[j][i] = rows[j]

# 			j += 1
# 		j = 0
# 		i += 1

	# But this line of magic also rotates the matrix.
	columns = list(zip(*game))	
	return checkRows(columns)

def checkDiag(game):
	if game[1][1] == 0:	#If the middle is 0, we can already tell there is no winner
		return 0
	if game [0][0] == game[1][1] == game[2][2]:
		if game[0][0] == 1:
			return("player_one")	#Give the number of the player that wins
		else:
			return("player_two")
	if game [0][2] == game[1][1] == game[2][0]:
		if game[1][1] == 1:
			return("player_one")	#Give the number of the player that wins
		else:
			return("player_two")



def checkForWinner(game):
	winner = checkRows(game)
	if winner:
		return winner
	
	winner = checkColumns(game)
	if winner:
		return winner
	
	winner = checkDiag(game)
	if winner:
		return winner
	
	# If we got to here without one of the other if-statements being true, it means there was no winner
	return("There was no winner")



	
if __name__ == '__main__':
	winner = checkForWinner(game)
	if winner:
		print(winner)
