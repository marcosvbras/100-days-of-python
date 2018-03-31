# coding=utf-8
"""Array II - Basic use with NumPy.

    Using NumPy for basic operations with arrays.
"""

import numpy

def run():
    # Creating a numpy.ndarray object with integers
    numbers = numpy.arange(10)
    print(numbers)
    # >>> [0 1 2 3 4 5 6 7 8 9]

    # Verifying the array dimensions
    print(numbers.shape)
    # >>> (10,)
    # This is an one-dimensional array with 10 elements

    # Changing the array dimension (Lines, Columns)
    numbers.shape = 2, 5
    print(numbers)
    # >>> [[0 1 2 3 4]
    #      [5 6 7 8 9]]

    # Showing the new array shape
    print(numbers.shape)
    # >>> (2, 5)
    # This is a multidimensional array with 2 lines and 5 columns

    # Printing the second line of the array
    print(numbers[1])
    # >>> [5 6 7 8 9]

    # Getting the element on position 1-2 (Line 2, column 3)
    print(numbers[1, 2])
    # >>> 7

    # Getting elements of the column 4
    print(numbers[:, 3])
    # >>> [3 8]

    # Creating a transposed Array
    print(numbers.transpose())
    # >>> [[0 5]
    #      [1 6]
    #      [2 7]
    #      [3 8]
    #      [4 9]]

if __name__ == '__main__':
    run()
