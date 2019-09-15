import numpy as np

'''
Build an array of 100 randomly chosen integers (any number from 1 to 100) 
and find the five largest numbers.
'''
x = np.random.randint(1, 101, size=100)
print(x)
#use the sort() to order all the numbers of tha array
x_in_order = np.sort(x)
print(x_in_order)
print(x_in_order[-5:])
