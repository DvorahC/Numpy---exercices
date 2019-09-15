import numpy as np

'''
Write a program that produces a one-dimensional array with 100 elements that are the even numbers between 2 and 200
'''
arr = np.arange(1, 200)
arr = (arr[arr % 2 == 0])
arr_count = len(arr)
print(arr)
print(f'This one dimensional array contains {arr_count} elements.')




