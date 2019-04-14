"""
Take two lists, and make a program that returns the list that contains only elements that are common
between these two lists, using at least one list comprehension.
"""

import random

a = sorted(random.sample(range(50), random.randint(5, 15)))
b = sorted(random.sample(range(50), random.randint(5, 15)))

print(a)
print(b)

print(set(elem for elem in a if elem in b))
