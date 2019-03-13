
import functools


def calc_values(x, y: int):
    print("X: {}  Y: {}".format(x, y))
    return x + y


numbers = [2, 3, 5, 8, 13]

# X becomes the sum of the elements then we add Y
reduced_value = functools.reduce(calc_values, numbers)
print(reduced_value)
