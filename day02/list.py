# coding=utf-8
"""Exploring basic data types with List."""


def add(characters):
    """Add some elements to list."""
    characters.append("Asuna")
    characters.append("Yui")
    characters.append("Mikasa")
    characters.insert(0, "Sakura")
    print("Elements added: {}".format(characters))


def slice(characters):
    """Use slice in a List."""
    print("First two elements: {}".format(characters[:2]))
    print("Ahead of the second element: {}".format(characters[2:]))
    print("Elements between second and fifth: {}".format(characters[2:5]))


def remove(characters):
    """Remove some list elements."""
    del characters[-1]
    print("Last element removed: {}".format(characters))
    print("One more removed: {}".format(characters.pop()))


if __name__ == '__main__':
    characters = ["Mashiro", "Yato", "Himiku", "Kaori", "Yuki"]
    print("Original list: {}".format(characters))
    print("First element: {}".format(characters[0]))
    print("Last element: {}".format(characters[-1]))
    add(characters)
    slice(characters)
    remove(characters)
