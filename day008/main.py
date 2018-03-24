# coding=utf-8
from collections import namedtuple


def run():
    # collections.namedtuple is a function of type Factory. It create a
    # tuple instance with field names and a class name

    # First parameter: class name
    # Second parameter: field list or string iterable object
    Profile = namedtuple('Profile', 'name age genre weight height')
    profile = Profile('Marcos Vinícius', 21, 'Male', 63, 173)
    print(profile.name)
    # >>> Marcos Vinícius

    print(Profile._fields)
    # >>> ('name', 'age', 'genre', 'weight', 'height')

    print(profile._asdict())
    # >>> OrderedDict([('name', 'Marcos Vinícius'), ('age', 21), ('genre', 'Male'), ('weight', 63), ('height', 173)])

    data = ('Foo Bar', 25, 'Male', 80, 180)
    # Creating a new named tuple
    profile = Profile._make(data)

    for key, value in profile._asdict().items():
        print("%s: %s" % (key, value))
        # name: Foo Bar
        # age: 25
        # genre: Male
        # weight: 80
        # height: 180


if __name__ == '__main__':
    run()
