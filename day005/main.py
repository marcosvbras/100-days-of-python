def run():
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    # Creating a new list with List Comprehension (listcomp)
    letters = [letter for letter in alphabet]
    print(letters)
    # >>> ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    # Using IF in a List Comprehension
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 10]
    odd_numbers = [number for number in numbers if number % 2 == 1]
    print(odd_numbers)
    # >>> [1, 3, 5, 7]

    # Using List Comprehension with 2 FOR
    columns = [1, 2, 3, 4, 5]
    lines = [10, 20, 30]
    mult = [(line, column) for line in lines for column in columns]
    print(mult)
    # >>> [(10, 1), (10, 2), (10, 3), (10, 4), (10, 5), (20, 1), (20, 2), (20, 3), (20, 4), (20, 5), (30, 1), (30, 2), (30, 3), (30, 4), (30, 5)]

    # Tips to keep concise and clear:
    #
    # 1 - If you won't do nothing with the created list, don't use listcomps
    # 2 - If the listcomp has more than 2 lines, break it in more pieces or use
    #     the normal FOR


if __name__ == '__main__':
    run()
