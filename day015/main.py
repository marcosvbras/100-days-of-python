# coding=utf-8
"""Day 015 - Set - Creation, Set Comprehensions and Operations

    This example covers the basic use of sets: the normal creation,
        the creation with Set Comprehensions, set operations and functions.

    NOTE: Sets are collections of unique objects and have the same maths
        operations.
"""


def run():
    ### Creating a new set

    ice_cream = {'vanilla', 'vanilla', 'strawberry', 'blackberry'}
    print(ice_cream)
    # >>> {'vanilla', 'strawberry', 'blackberry'}

    # Empty set
    foobar = set()
    print(foobar)
    # >>> set()

    # Set Comprehensions
    numbers = { number for number in range(10) }
    print(numbers)
    # >>> {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

    # Removing list duplicated items and converting to set
    to_do_list_raw = ['eat', 'eat', 'sleep', 'sleep', 'code', 'repeat']
    to_do_list = set(to_do_list_raw)
    print(to_do_list)
    # >>> {'sleep', 'eat', 'code', 'repeat'}

    ### Using set operations

    set_a = { 0, 1, 2, 3, 4, 5, 6}
    set_b = { 2, 3, 5, 7, 8, 9}

    union = set_a | set_b
    print(union)
    # >>> {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

    intersection = set_a & set_b
    print(intersection)
    # >>> {2, 3, 5}

    # Another way to do an intersection
    # It is heviest to do an intersection this way instead the way above.
    intersection = set_a.intersection(set_b)
    print(intersection)
    # >>> {2, 3, 5}

    difference = set_a - set_b
    print(difference)
    # >>> {0, 1, 4, 6}

    a = {1, 2, 3}
    b = {1, 2, 3, 4, 5}

    is_subset = a <= b
    print(is_subset)
    # >>> True

    is_subset = b <= a
    print(is_subset)
    # >>> False

    is_sub = a < b
    print(is_sub)
    # >>> True

    is_sub = b < a
    print(is_sub)
    # >>> False

    is_superset = a >= b
    print(is_superset)
    # >>> False

    is_superset = b >= a
    print(is_superset)
    # >>> True

    is_super = a > b
    print(is_super)
    # >>> False

    is_super = b > a
    print(is_super)
    # >>> True

    # Remove the first element and return it
    print(set_a.pop())
    # >>> 0
    print(set_a)
    # >>> {1, 2, 3, 4, 5, 6}

    set_a.remove(6)
    print(set_a)
    # >>> {1, 2, 3, 4, 5}

    # Clear all elements
    set_b.clear()
    print(set_b)
    # set()


if __name__ == '__main__':
    run()
