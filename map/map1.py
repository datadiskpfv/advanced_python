import timeit

text = "what have the romans ever done for us"

# Using comprehensions
def comp_caps():
    capitals = [char.upper() for char in text]
    return capitals


def comp_words():
    words = [word.upper() for word in text.split(' ')]
    return words


# Using Map to produce the same as above
def map_caps():
    mcapitals = list(map(str.upper, text))
    return mcapitals


def map_words():
    mwords = list(map(str.upper, text.split(' ')))
    return mwords


if __name__ == '__main__':
    print(comp_caps())
    print(comp_words())
    print(map_caps())
    print(map_words())

    print(timeit.timeit(comp_caps, number=1000))
    print(timeit.timeit(map_caps, number=1000))

    print(timeit.timeit(comp_words, number=1000))
    print(timeit.timeit(map_words, number=1000))




