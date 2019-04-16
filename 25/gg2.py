"""
Write a guessing game where the user knows the correct number, and the code tries to find it
The user will have to input if the number is correct or not
"""
import random



def main():
	num_tries = 0
	lowest_possible = 0
	highest_possible = 1000
	guess = random.randint(450,550)
	updown = ""
	print("Welcome to 'Guessing game 2!'")
	print("Think of a number between 0 and 1000, and ill try to guess it in as few tries as possible")



	while updown != "y":
		num_tries += 1

		if updown == "up":
			lowest_possible = guess
			guess = (lowest_possible + ((highest_possible - lowest_possible)/2))
		
		elif updown == "down":
			highest_possible = guess
			guess = (lowest_possible + ((highest_possible - lowest_possible)/2))

		print("lowest_possible: " + str(lowest_possible))
		print("highest_possible: " + str(highest_possible))
		updown = input("I guess " + str(int(guess)) + " is this correct? Tell me 'y', 'up' or 'down':  ")


	if updown == "y":
		print("I win, with " + str(num_tries) +" tries!")
		return


if __name__ == "__main__":
	main()