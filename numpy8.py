import numpy as np
'''
Write a function that accepts a NumPy array that represents an X-Circle board 
and returns True if there is a winner in the game. 
 '''

def is_there_a_winner(a):
    good_line = np.array(['X', 'X', 'X'])
    rows = a[0:, :]
    columns = a[:, 0:]
    if (rows == good_line).all(axis=1).any() or(a.diagonal() == good_line).all() or (columns == good_line).all(axis=0).any():
        return True
    else:
        return False


a = np.array([
  ['X', ' X', ' '],
  [' ', '', 'O'],
  ['X', ' ', 'X']
])

print(is_there_a_winner(a))

