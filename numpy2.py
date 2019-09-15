import numpy as np

'''
Build a 10 by 10 NumPy array that represents the multiplication table

'''
a = np.arange(1, 11)
b = a.reshape(10, 1)
arr_full = a * b
print(arr_full)
