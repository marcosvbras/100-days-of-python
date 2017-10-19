"""Use string interpolation."""


def interpolate(word1, word2):
    """Print a sentence with different types of string interpolation."""
    print("First word: {} - Second word: {}".format(word1, word2))
    print("First word: {0} - Second word: {1}".format(word1, word2))
    print("First word: %(word1)s - Second word: %(word2)s" % {'word1':word1, 'word2':word2})
    print("First word: %s - Second word: %s" % (word1, word2))


if __name__ == '__main__':
    print("Interpolating with 4 ways:")
    interpolate("Ruby", "Go")
