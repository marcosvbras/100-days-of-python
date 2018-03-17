from fruits import FruitPack
from random import choice


def test():
    fruit_pack = FruitPack()

    print("All fruits: ")
    for fruit in fruit_pack:
        print(fruit)

    print("FruitPack length: %d" % len(fruit_pack))
    print("FruitPack first item: %s" % fruit_pack[0])
    print("FruitPack first-two item: %s" % fruit_pack[0:2])
    print("Random fruit: %s" % choice(fruit_pack))
    print(
        "Is Lemon in FruitPack? %s" % "True" if "Lemon" in fruit_pack else "False"
    )

if __name__ == '__main__':
    test()
