# coding=utf-8
"""List I - Append, Insert and Del.

    Exploring basic data types with List.
"""


def add(characters):
    """Add some elements to list."""
    characters.append("Asuna")
    characters.append("Yui")
    characters.append("Mikasa")
    characters.insert(0, "Sakura")
    print("New list: {}".format(characters))
    # >>> New list: ['Sakura', 'Mashiro', 'Yato', 'Himiku', 'Kaori', 'Yuki', 'Asuna', 'Yui', 'Mikasa']


def slice(characters):
    """Use slice in a List."""
    print("First two elements: {}".format(characters[:2]))
    # >>> First two elements: ['Sakura', 'Mashiro']
    print("Ahead of the second element: {}".format(characters[2:]))
    # >>> Ahead of the second element: ['Yato', 'Himiku', 'Kaori', 'Yuki', 'Asuna', 'Yui', 'Mikasa']
    print("Elements between second and fifth: {}".format(characters[2:5]))
    # >>> Elements between second and fifth: ['Yato', 'Himiku', 'Kaori']


def remove(characters):
    """Remove some list elements."""
    print("Last element removed: {}".format(characters.pop()))
    # >>> Last element removed: Mikasa
    del characters[-1]
    print("New list: {}".format(characters))
    # >>> New list: ['Sakura', 'Mashiro', 'Yato', 'Himiku', 'Kaori', 'Yuki', 'Asuna']


if __name__ == '__main__':
    characters = ["Mashiro", "Yato", "Himiku", "Kaori", "Yuki"]
    print("Original list: {}".format(characters))
    # >>> Original list: ['Mashiro', 'Yato', 'Himiku', 'Kaori', 'Yuki']
    print("First element: {}".format(characters[0]))
    # >>> First element: Mashiro
    print("Last element: {}".format(characters[-1]))
    # >>> Last element: Yuki
    add(characters)
    slice(characters)
    remove(characters)
