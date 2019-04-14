"""
Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message
of congratulations to the winner, and ask if the players want to start a new game)
"""
import time
import random

def draw(p1, p2):
    print("\nyou both chose " + p1 + " so its a draw!")
    
def p1_wins(p1, p2):
    print(p1 + " wins over " + p2 + " therefore player 1 wins!")
    
def p2_wins(p1, p2):
    print(p2 + " wins over " + p1 + " therefore teh Computer wins!")

rps = ["rock", "paper", "scissor"]
    
print ("welcome to this game of rock - paper - scissors!\n")


while 1:
    p1 = input("Player 1 enter your choice: ")
    if p1 != "rock" and p1 != "paper" and p1 != "scissor":
        print("You need to write 'rock', 'paper' or 'scissor'")
        break
    p2 = rps[random.randint(0,2)]
    time.sleep(0.5)
    print("\nThe computer choose: ") 
    time.sleep(2)
    print(p2)
    time.sleep(1)
    
    
    if p1 == p2:
        draw(p1,p2)    
    
    elif (p1 == "rock" and p2 == "scissor") or (p1 == "paper" and p2 == "rock") or (p1 == "scissor" and p2 == "paper"):
        p1_wins(p1, p2)
    else:
        p2_wins(p1, p2)
    
    
       
    
    usrinp = input("\n\nDo you want to play another game? y/n ")
    if usrinp == "n":
        break