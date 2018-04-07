# coding=utf-8
"""Day 017 - Some great built-in functions.

    This example covers some useful built-in functions.
"""

def run():
    # Gettings absolute values
    """In mathematics, absolute value refers to the distance that a number is on the number line from 0. Absolute value does not take into consideration which direction from zero the number lies, meaning that negative numbers will be represented with positive numbers."""
    print(abs(5))
    # >>> 5
    print(abs(-5))
    # >>> 5
    print(abs(2.5))
    # >>> 2.5
    print(abs(-24.6))
    # >>> 24.6

    # Return a tuple with quotient and remainder from division of the first parameter and the second one
    print(divmod(5, 2))
    # >>> (2, 1)

    # Rounding numbers
    # The round() function takes in two numbers, one to be rounded, and one with the number of decimal places to include
    print(round(11.6663, 3))
    # >>> 11.666
    print(round(11.6665, 3))
    # >>> 11.666
    print(round(11.6666, 3))
    # >>> 11.667

    bills = [2, 5, 10, 20, 50, 100]

    # Calculating a Sum from lists and dicts
    print(sum(bills))
    # >>> 187

    # Getting the minimum and maximum numbers
    print(min(bills))
    # >>> 2
    print(max(bills))
    # >>> 100

    # Creating sequences. Parameters: start, stop, step
    print(list(range(5)))
    # >>> [0, 1, 2, 3, 4]
    print(list(range(1, 5)))
    # >>> [1, 2, 3, 4]
    print(list(range(1, 10, 2)))
    # >>> [1, 3, 5, 7, 9]

    # Aggregating elements from each iterator
    names = ['Marcos', 'Irene', 'Peter', 'Minah']
    ages = [21, 26, 30, 24]
    countries = ['Brazil', 'South Korea', 'United States', 'South Korea']
    people = zip(names, ages, countries)

    for item in people:
        print(item)
    # ('Marcos', 21, 'Brazil')
    # ('Irene', 26, 'South Korea')
    # ('Peter', 30, 'United States')
    # ('Minah', 24, 'South Korea')


if __name__ == '__main__':
    run()
