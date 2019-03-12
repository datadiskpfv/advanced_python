import timeit

setup = """\
locations = {0: "You are sitting in front of a computer learning Python",
             1: "You are standing at the end of a road before a small brick building",
             2: "You are at the top of a hill",
             3: "You are inside a building, a well house for a small stream",
             4: "You are in a valley beside a stream",
             5: "You are in the forest"}

exits = {0: {"Q": 0},
         1: {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
         2: {"N": 5, "Q": 0},
         3: {"W": 1, "Q": 0},
         4: {"N": 1, "W": 2, "Q": 0},
         5: {"W": 2, "S": 1, "Q": 0}}
"""

locations = {0: "You are sitting in front of a computer learning Python",
             1: "You are standing at the end of a road before a small brick building",
             2: "You are at the top of a hill",
             3: "You are inside a building, a well house for a small stream",
             4: "You are in a valley beside a stream",
             5: "You are in the forest"}

exits = {0: {"Q": 0},
         1: {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
         2: {"N": 5, "Q": 0},
         3: {"W": 1, "Q": 0},
         4: {"N": 1, "W": 2, "Q": 0},
         5: {"W": 2, "S": 1, "Q": 0}}

nested_loop = """\
for loc in sorted(locations):
    exits_to_destination_1 = []
    for xit in exits:
        if loc in exits[xit].values():
            exits_to_destination_1.append((xit, locations[xit]))
"""
# removed below from above to test true performance speed
# print("Locations leading to {}".format(loc), end='\t')
# print(exits_to_destination_1)


def nested_loop_def():
    for loc in sorted(locations):
        exits_to_destination_1 = []
        for xit in exits:
            if loc in exits[xit].values():
                exits_to_destination_1.append((xit, locations[xit]))
    # print("Locations leading to {}".format(loc), end='\t')
    # print(exits_to_destination_1)


comprehension_loop = """\
for loc in sorted(locations):
    exits_to_destination_2 = [(xit, locations[xit]) for xit in exits if loc in exits[xit].values()]
"""
# removed below from above to test true performance speed
# print("Locations leading to {}".format(loc), end='\t')
# print(exits_to_destination_2)

nested_comprehension_loop = """\
exits_to_destination_3 = [[(xit, locations[xit]) for xit in exits if loc in exits[xit].values()]
                          for loc in sorted(locations)]
"""
# removed below from above to test true performance speed
# for index, loc in enumerate(exits_to_destination_3):
# print("Locations leading to {}".format(index), end='\t')
# print(loc)

# Generator is faster in building but slower in looping over
nested_generator_loop = """\
exits_to_destination_3 = ([(xit, locations[xit]) for xit in exits if loc in exits[xit].values()]
                          for loc in sorted(locations))
"""


number = 100000

# result1 = timeit.timeit(nested_loop, globals=globals(), number=1000) use globals with python 3.5 up
result1 = timeit.timeit(nested_loop, setup, number=number)          # using string
result1a = timeit.timeit(nested_loop_def, setup, number=number)     # using function

result2 = timeit.timeit(comprehension_loop, setup, number=number)
result3 = timeit.timeit(nested_comprehension_loop, setup, number=number)
result4 = timeit.timeit(nested_generator_loop, setup, number=number)

print("Nested Loop:\t\t\t\t{}".format(result1))
print("Nested Loop Function:\t\t{}".format(result1a))
print("Comprehension Loop:\t\t\t{}".format(result2))
print("Nested Comprehension Loop:\t{}".format(result3))
print("Nested Generator Loop:\t\t{}".format(result4))
