"""
Write a program (using functions!) that asks the user for a long string containing multiple words. 
Print back to the user the same string, except with the words in backwards order.
"""

def giveReverse(s):
    s = s.split()
    s.reverse()
    return s
 
    

inp = str(input("Write your sentence here and i will print it back in reverse order:\n"))

reversed = giveReverse(inp)
reversed = ' '.join(reversed)
print(reversed)
