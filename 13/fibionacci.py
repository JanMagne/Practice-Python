"""
Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. 
Take this opportunity to think about how you can use functions.
"""



def getFib(n):
    fibolast = -1
    fibocurr = 1
    fibolist = []
    
    for i in range(n):
        fibo = fibolast + fibocurr
        fibolast = fibocurr
        fibocurr = fibo
        fibolist.append(fibo)
    
    return fibolist
        
        


userinput = int(input("How many fibionacci numbers do you need? "))
fibolist = getFib(userinput)
print (fibolist)




