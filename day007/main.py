# coding=utf-8

def run():
    full_name = ('Marcos', 'Oliveira',)
    # Parallel Assignment
    first_name, last_name = full_name
    print("Name: %s %s" % (first_name, last_name))
    # >>> Marcos Oliveira

    a = 1
    b = 5
    # Changing values among variables without a temp variable
    a, b = b, a
    print((a, b))
    # >>> (5, 1)

    numbers = (5, 4,)
    print(sum(*numbers))
    # >>> 9

    state = ('BR', 'Brazil',)
    # Omitting the first tuple element
    _, title = state
    print(title)
    # >>> Brazil

    fruits = ['Strawberry', 'Watermelon', 'Kiwiifruit', 'Coconut', 'Apple']
    first, second, *other = fruits
    print((first, second, other))
    # >>> ('Strawberry', 'Watermelon', ['Kiwiifruit', 'Coconut', 'Apple'])
    *first_three, penult, last = fruits
    print((first_three, penult, last))
    # >>> (['Strawberry', 'Watermelon', 'Kiwiifruit'], 'Coconut', 'Apple')

def sum(num1, num2):
    """Return the sum between num1 and num2."""
    return num1 + num2

if __name__ == '__main__':
    run()
