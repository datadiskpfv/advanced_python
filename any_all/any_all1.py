entries1 = [1, 2, 3, 4, 5, False]
print("all: {}".format(all(entries1)))       # One is false
print("any: {}".format(any(entries1)))       # one element is True (number is True)
print("-" * 30)

entries2 = [0, 1, 2, 3, 4, 5]
print("all: {}".format(all(entries2)))       # 0 is false
print("any: {}".format(any(entries2)))       # one element is True (number is True)
print("-" * 30)

entries3 = [0]
print("all: {}".format(all(entries3)))       # 0 is false
print("any: {}".format(any(entries3)))       # 0 is False and we have no True elements
print("-" * 30)

entries4 = []
print("all: {}".format(all(entries4)))       # empty list is True for all
print("any: {}".format(any(entries4)))       # empty list is False for any
print("-" * 30)
