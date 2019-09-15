import numpy as np

'''
Build an array of 10 randomly selected integers (any number from 1 to 100) and print out only the odd numbers.
'''

x = np.random.randint(1, 101, size=10)
print(x)
print(x[x % 2 == 1])
