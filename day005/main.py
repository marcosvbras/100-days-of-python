def run():
    # Tips to keep concise and clear:
    #
    # 1 - If you won't do nothing with the created list, don't use listcomps
    # 2 - If the listcomp has more than 2 lines, break it in more pieces or use
    #     the normal FOR

    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    # Creating a new list with List Comprehension (listcomp)
    letters = [letter for letter in alphabet]
    print(letters)

    # Using IF in a List Comprehension
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 10]
    odd_numbers = [number for number in numbers if number % 2 == 1]
    print(odd_numbers)

    # Using List Comprehension with 2 FOR
    columns = [1, 2, 3, 4, 5]
    lines = [10, 20, 30]
    mult = [(line, column) for line in lines for column in columns]
    print(mult)


if __name__ == '__main__':
    run()
