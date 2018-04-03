# coding=utf-8
"""Day 014 - setdefault: When dict.get it's a bad idea.

    This example covers the difference between dict.get and dict.setdefault functions.

    Setdefault is a function that is more efficient that dict.get,
    because it already set a default value if the key doesn't exists
    and return the value.
"""


def run():
    netflix = { 'movies': ['Star Wars', 'The Martian', 'Interestelar'] }

    # Nothing efficient way to non existent keys with dict.get
    tv_shows = netflix.get('tv_shows', [])
    tv_shows.append('How I Met Your Mother')
    netflix['tv_shows'] = tv_shows
    print(netflix)
    # >>> {'movies': ['Star Wars', 'The Martian', 'Interestelar'], 'tv_shows': ['How I Met Your Mother']}

    ### Efficient way to non existent keys with dict.setdefault
    netflix.setdefault('animes', []).append('Sakurasou no Pet na Kanojo')
    print(netflix)
    # >>> {'movies': ['Star Wars', 'The Martian', 'Interestelar'], 'tv_shows': ['How I Met Your Mother'], 'animes': ['Sakurasou no Pet na Kanojo']}

if __name__ == '__main__':
    run()
