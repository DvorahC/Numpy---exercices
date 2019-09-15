import numpy as np

'''
From the multiplication table array in exercice numpy2, 
print only the diagonals (ie only numbers 1, 4, 9, 16 and so on). Use the Boolean Mask.
'''
#NOT DONE

a = np.arange(1, 11)
b = a.reshape(10, 1)
arr_full = a * b
print(arr_full)
