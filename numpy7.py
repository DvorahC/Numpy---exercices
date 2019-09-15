import numpy as np
'''
Update exercice numpy6 to show the five largest unique numbers.

 '''
x = np.random.randint(1, 101, size=100)
print(x)
#use the sort() to order all the numbers of tha array
x_in_order = np.sort(x)
print(x_in_order)
print(np.unique(x_in_order)[-5:])

