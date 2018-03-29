# coding=utf-8

def run():
    anime = "Ano Hi Mita Hana no Namae Bokutachi Wa Mada Shiranai"

    print(anime[:8])
    # >>> Ano H
    print(anime[7:])
    # >>> Mita Hana no Namae Bokutachi Wa Mada Shiranai
    print(anime[0:11])
    # >>> Ano Hi Mita
    print(anime[7::20])

    letters = "AaaaaBbbbbCccccDddddEeeeeF"
    # Skiping every 5 itens slice[start:stop:step]
    print(letters[::5])
    # >>> ABCDEF
    # Skiping every 5 itens (reverse) slice[start:stop:step]
    print(letters[::-5])
    # >>> FEDCBA

    numbers = list(range(10))
    # Original list
    print(numbers)
    # >>> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    # Replacing items from 2 until 5 index
    numbers[5:8] = [100, 200]
    print(numbers)
    # >>> [0, 1, 2, 3, 4, 100, 200, 8, 9]

    del numbers[0:3]
    print(numbers)
    # >>> [3, 4, 100, 200, 8, 9]


if __name__ == '__main__':
    run()
