"""
In this exercise, the task is to write a function that picks a 
random word from a list of words from a file. Each line in the 
file is a new word.
"""
import random

MAX_GUESSES = 6


def pickWord(filename):
	words = []
	with open(filename, "r") as f:
		for line in f:
			words.append(f.readline().strip())

	return words[random.randint(0, len(words))]


def usrInp(clue, guessed):
	guess = input("Guess your letter: ")
	
	if guess in guessed["guessedCorrect"]:		#Did the user already guess this correct letter?
		print("You have already guessed this, it's there see?")
		return guessed

	if guess in guessed["guessedWrong"]:		#Dis the user already guess this Incorrect letter?
		print("You have already guessed this letter, its NOT in the word")
		return guessed


	if guess in clue: #Is the guessed letter in the word or not?
		print("The letter '" + guess +"' is in the word!")
		guessed["guessedCorrect"].add(guess)
	else:
		print("The letter '" + guess +"' is NOT in the word!")
		guessed["guessedWrong"].add(guess)
	
	return guessed


def printHangman(clue, guessed):
	print ("\n")

	for letter in clue:
		if letter in guessed["guessedCorrect"]:
			print(letter + " ", end="")
		else:
			print("_ ", end="")

	print ("\n")


def welcome():
	print("""
 _		                                               
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                                                         
          
		""")

def main():
	welcome()
	corrSet = set()
	wrongSet = set()
	guessDict = {"guessedWrong":wrongSet, "guessedCorrect":corrSet}

	clue_word = pickWord("scrabble.txt")
	clue_wordSet = set(clue_word)
	print("The word has " + str(len(clue_word)) + " letters.")
	print("You have " + str(MAX_GUESSES) + " chances.")
	#print(clue_word)

	while 1:
		guessDict = usrInp(clue_word, guessDict)

		printHangman(clue_word, guessDict)

		if len(clue_wordSet) == len(guessDict["guessedCorrect"]):
			print("You have guessed all letters of the hangman. Congrats, you WIN")
			exit()

		if len(guessDict["guessedWrong"]) >= MAX_GUESSES:
			print("""
				  _______
			     |/      |
			     |      (_)
			     |    '\'|/
			     |       |
			     |      / \
			     |
			 	_|___
				""")
			print("You have to many wrong guesses and have lost the game")

			break



if __name__ == '__main__':
	main()