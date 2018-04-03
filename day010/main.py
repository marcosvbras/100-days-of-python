# coding=utf-8
"""Array I - Tired of lists? Use Arrays!.

    For store only numbers, most of times is better use an Array.
    It accepts all mutable sequences functions.
"""

from array import array
from random import random

def run():
    """
        Type Codes for array:
            'b': signed integer (Minimum size in bytes: 1)
            'B': unsigned integer (Minimum size in bytes: 1)
            'u': Unicode character (Minimum size in bytes: 2)
            'h': signed integer (Minimum size in bytes: 2)
            'H': unsigned integer (Minimum size in bytes: 2)
            'i': signed integer (Minimum size in bytes: 2)
    """
    numbers = array('d', (random() for i in range(10**5)))
    print(numbers)
    # >>> array('d', [..., 0.12960939888637146, 0.8041282435622599])

    print(numbers[0])
    # 0.579947919425


if __name__ == '__main__':
    run()
