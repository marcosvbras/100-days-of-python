# coding=utf-8
"""Day 013 - Dicts I - Simple creation and Dict Comprehensions.

    This example covers the creation of an important Python data type: Dict.
    As a plus, there is an example of Dict creation with Dict Comprehensions.
"""


def run():
    ### Creating dicts

    framework = dict(name='Flask', language='Python', cool=True)
    print(framework)
    # >>> {'language': 'Python', 'cool': True, 'name': 'Flask'}

    person = {
        'name': 'Marcos Vinícius',
        'age': 21,
        'weight': 63,
        'height': 173
    }
    print(person)
    # >>> {'age': 21, 'name': 'Marcos Vinícius', 'height': 173, 'weight': 63}

    preferences = dict(
        zip(['food', 'color', 'movie'], ['pizza', 'blue', 'Star Wars'])
    )
    print(preferences)
    # >>> {'food': 'pizza', 'color': 'blue', 'movie': 'Star Wars'}

    ### Using Dict Comprehensions (dictcomp)

    countries = [
        ('BRA', 'Brazil'),
        ('USA', 'United States'),
        ('MEX', 'México'),
        ('CAN', 'Canada')
    ]
    country_initials = {country: initials for initials, country in countries}
    print(country_initials)
    # >>> {'México': 'MEX', 'United States': 'USA', 'Canada': 'CAN', 'Brazil': 'BRA'}


if __name__ == '__main__':
    run()
