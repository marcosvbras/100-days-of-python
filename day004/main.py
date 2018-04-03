"""Day 004 - Everything can be an iterable.

    This example covers how to make iterable an non built-in class.
"""
from fruits import FruitPack
from random import choice


def run():
    fruit_pack = FruitPack()

    print("All fruits: ")
    for fruit in fruit_pack:
        print(fruit)
        # >>> All fruits:
        #     Strawberry
        #     Grape
        #     Kiwifruit
        #     Blackberry
        #     Orange
        #     Watermelon
        #     Apple
        #     Lemon
        #     Papaya
        #     Cherry

    print("FruitPack length: %d" % len(fruit_pack))
    # >>> FruitPack length: 10
    print("FruitPack first item: %s" % fruit_pack[0])
    # >>> FruitPack first item: Strawberry
    print("FruitPack first-two item: %s" % fruit_pack[0:2])
    # >>> FruitPack first-two item: ['Strawberry', 'Grape']
    print("Random fruit: %s" % choice(fruit_pack))
    print(
        "Is Lemon in FruitPack? %s" % "True" if "Lemon" in fruit_pack else "False"
    )
    # >>> Is Lemon in FruitPack? True

if __name__ == '__main__':
    run()
