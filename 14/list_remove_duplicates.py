"""
Write a program that takes a list and returns a new list that contains all the elements 
in the first list minus all duplicates.
Extra: Write two different functions to do this - one using a loop and constructing a list, and another using sets.
"""
import random


def newList(length=10):
    a = []
    for i in range(length):
        a.append(random.randint(1, 10))
    a = sorted(a)
    return a


def removeDupUsingSet(l):
    return set(l)

def removeDupUsingList(li):
    for elem in li:
        if li.count(elem) > 1:
            li.remove(elem)
    
    return li
    



mylist = newList()
i = mylist
j = mylist
print(mylist)

x = removeDupUsingSet(i)
y = removeDupUsingList(j)

print("Removed duplicates using sets:  " + str(x))
print("Removed duplicates using lists: " + str(y))



