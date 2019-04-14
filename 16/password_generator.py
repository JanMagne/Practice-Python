"""
Make a password generator. Strong passwords has a mix of lowercase, uppercase, numbers and symbols.

Extra:
Ask the user how strong a password he wants
"""

import random
import string
import time

def createPassword(letters, num_char):
    # Takes in a list or string of lettes to use for the pw, and the lenght of the pw
    password = list()
    pw = " "
    for x in range (0, num_char):
        password.append(letters[random.randint(0, len(letters)-1)])

    
    pw = pw.join(password)
    pw = pw.replace(" ","")
    
    return pw

def main():
    print("Hey guy, ill make a password for you")
    num_char = int(input("How long would you like your pw to be?\n"))
    strenght = int(input("OK, how strong do you want the password to be, from 0 to 3?"))
    print(str(strenght))

    super_weak_candidates = ("passord","admin","1234")
    weak_candidates = string.ascii_lowercase
    medium_candidates = weak_candidates + string.digits
    strong_candidates = string.ascii_letters + string.punctuation + string.digits
    
    strong_candidates = list(strong_candidates)

    if strenght == 0:
        password = super_weak_candidates[random.randint(0,len(super_weak_candidates)-1)]
    if strenght == 1:
        password = createPassword(weak_candidates, num_char)
    if strenght == 2:
        password = createPassword(medium_candidates, num_char)
    if strenght == 3:
        password = createPassword(strong_candidates, num_char)
    
    
    print("\nHere is your password:\n" + password)

    
    time.sleep(5)

main()
