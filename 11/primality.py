"""
Ask the user for a number and determine whether the number is prime or not.
"""


def findDivisors(c):
    divisors = []
    for x in range((c//2)+1):
    
        #Dont check for 0 or 1
        if x == 0 or x == 1:
            continue
        
        if c % x == 0:
            divisors.append(x)
    
    #Insert 1 as the first divisor
    divisors.insert(0, 1) 
    return divisors
            
    
    
candidate = int(input("Insert a number and ill tell you if its a prime number or not: "))

divisors = findDivisors(candidate)
if divisors == [1]:
    print(str(candidate) + " is a prime number")
else:
    print(str(candidate) + " is not a prime number, its divisors are: ")
    print(divisors)