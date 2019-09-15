import numpy as np
'''

Build an array of 10 randomly selected integers (any number from 1 to 100)
and find the smallest number greater than 50
 '''
x = np.random.randint(1, 101, size=10)
print(x)
print(min(x[x > 50]))
