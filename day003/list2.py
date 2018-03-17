# coding=utf-8
"""Exploring 'magic' methods with List."""


def do_something_magical(animes, tvshows):
    """Use some list methods."""
    animes.reverse()
    print("Inverted anime list: {}".format(animes))
    tvshows.sort()
    print("Sorted TV Shows list: {}".format(tvshows))
    animes.extend(tvshows)
    new_list = animes
    print("Concatenated lists: {}".format(new_list))


if __name__ == '__main__':
    animes = ["Shingeki no Kyojin", "Shigatsu Wa Kimi No Uso",
              "Sakurasou no Pet na Kanojo"]
    tvshows = ["Star Wars", "Pirates Of The Caribean", "Sherlock Holmes"]
    print("Original Anime List: {}".format(animes))
    print("Original TV Shows List: {}".format(tvshows))
    do_something_magical(animes, tvshows)
