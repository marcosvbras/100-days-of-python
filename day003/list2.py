# coding=utf-8
"""Exploring 'magic' methods with List."""


def do_something_magical(animes, tvshows):
    """Use some list methods."""
    animes.reverse()
    print("Inverted anime list: {}".format(animes))
    # >>> Inverted anime list: ['Sakurasou no Pet na Kanojo', 'Shigatsu Wa Kimi No Uso', 'Shingeki no Kyojin']
    tvshows.sort()
    print("Sorted TV Shows list: {}".format(tvshows))
    # >>> Sorted TV Shows list: ['Pirates Of The Caribean', 'Sherlock Holmes', 'Star Wars']
    animes.extend(tvshows)
    new_list = animes
    print("Concatenated lists: {}".format(new_list))
    # >>> Concatenated lists: ['Sakurasou no Pet na Kanojo', 'Shigatsu Wa Kimi No Uso', 'Shingeki no Kyojin', 'Pirates Of The Caribean', 'Sherlock Holmes', 'Star Wars']


if __name__ == '__main__':
    animes = ["Shingeki no Kyojin", "Shigatsu Wa Kimi No Uso",
              "Sakurasou no Pet na Kanojo"]
    tvshows = ["Star Wars", "Pirates Of The Caribean", "Sherlock Holmes"]
    print("Original Anime List: {}".format(animes))
    # >>> Original Anime List: ['Shingeki no Kyojin', 'Shigatsu Wa Kimi No Uso', 'Sakurasou no Pet na Kanojo']
    print("Original TV Shows List: {}".format(tvshows))
    # >>> Original TV Shows List: ['Star Wars', 'Pirates Of The Caribean', 'Sherlock Holmes']
    do_something_magical(animes, tvshows)
