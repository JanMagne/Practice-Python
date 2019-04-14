"""
Write a program that takes a list of numbers and makes a new list of only the first 
and last elements of the given list. For practice, write this code inside a function.
"""

import random


def giveEnds(li):
    return [li[0], li[-1]]

a = random.sample(range(50),5)
b = giveEnds(a)
print (a)
print (b)

