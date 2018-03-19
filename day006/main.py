# coding=utf-8

def run():
    # Attributing tuple values in variables
    name, age, height, weight = ('Marcos', 21, 173, 62)
    print("Name: {} - Age: {} - Height: {} - Weight: {}".format(
        name, age, height, weight)
    )
    # >>> Name: Marcos - Age: 21 - Height: 173 - Weight: 62

    animes = (
        ('Attack on Titan', 'Seinen'),
        ('Sakurasou no Pet na Kanojo', 'Slice Of Life'),
        ('Fullmetal Alchemist', 'Shonen'),
    )

    for anime in animes:
        # The operator '%' understand the tuple 'anime' as separated fields
        print("%s/%s" % anime)
        # >>> Attack on Titan/Seinen
        #     Sakurasou no Pet na Kanojo/Slice Of Life
        #     Fullmetal Alchemist/Shone

    cities = ['Porto Alegre', 'Rio de Janeiro', 'Minas Gerais']
    # Creating a tuple with Generator Expressions (genexp)
    # Generator Expressions are used to create sequences like Tuple
    cities_tuple = tuple(city for city in cities)
    print(cities_tuple)
    # >>> ('Porto Alegre', 'Rio de Janeiro', 'Minas Gerais')

if __name__ == '__main__':
    run()
