__author__ = 'Eyob Woldeghebriel'

import numpy as n

def kramer(a):
    row = 0
    column = 0

    if a.shape == (2, 2):
        print(a)

    else:
        for i in range(0, a.size):
            b = n.copy(a)
            b = n.delete(b, row, axis=0)
            b = n.delete(b, column, axis=1)
            kramer(b)
            column += 1

            if column == (a.size ** 0.5):
                column = 0
                row += 1

a = n.matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
b = n.matrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
c = n.matrix([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]])

kramer(a)



