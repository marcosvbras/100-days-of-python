# coding=utf-8
"""Day 018 - String II - Useful functions

    This example covers a bunch of great String functions.
"""

def run():
    # These functions below are not in-place. The value of the variables does not change.

    # The first letter of the first word to up
    print("marcos".capitalize())
    # >>> 'Marcos'

    # The first letter of each word to up
    print("marcos vinicius".title())
    # >>> 'Marcos Vinicius'

    # Lowercase
    print("MARCOS".lower())
    # >>> 'marcos'

    # Uppercase
    print("marcos".upper())
    # >>> MARCOS

    # Removing blank spaces sorround and things like that
    print("\n   marcos  \t\t".strip())
    # >>> 'marcos'

    # Getting the index of some letter
    print("marcos".index('s'))
    # >>> 5

    # Counting occurrences
    print("haha hehehe hihihihihi".count("he"))
    # >>> 3

    # Replacing words
    print("Potato is an amazing fruit!".replace("Potato", "Kiwifruit"))
    # >>> 'Kiwifruit is an amazing fruit!'

    # Getting a list of substrings separated by the given delimiter
    print("Marcos-Vinícius-Brás-de-Oliveira".split("-"))
    # >>> ['Marcos', 'Vinícius', 'Brás', 'de', 'Oliveira']

    # Searches for the given string and returns the first index where it begins or -1 if not found
    print("This string is amazing".find("string"))
    # >>> 5

    # Converting some value to String
    print(str(False))
    # >>> 'False'

    print("this is a toggle string case".swapcase())
    # >>> 'THIS IS A TOGGLE STRING CASE'

    ### Verifications

    print("5".isdigit())
    # >>> True
    print("marcos".isdigit())
    # >>> False

    print(" ".isspace())
    # >>> True
    print("marcos ".isspace())
    # >>> False

    # Returns True if it has at least 1 character and all alphanumeric
    print("Python".isalnum())
    # >>> True
    print("///".isalnum())
    # >>> False

    # Returns True if it has at least 1 character and all alphabetic
    print("Ruby".isalpha())
    # >>> True
    print("Ruby555".isalpha())
    # >>> False

    print("swift".islower())
    # >>> True

    print("katiau".isupper())
    # >>> False

    print("4".isnumeric())
    # >>> True
    print("4.3".isnumeric())
    # >>> False

    print("Marcos Vinícius".istitle())
    # >>> True
    print("Marcos vinícius".istitle())
    # >>> False

    print("strawberry".startswith('straw'))
    # >>> True

    print("strawberry".endswith('straw'))
    # >>> False


if __name__ == '__main__':
    run()
