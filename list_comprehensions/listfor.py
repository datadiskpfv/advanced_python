print(__file__)

numbers = [1, 2, 3, 4, 5, 6]

squares = []

for number in numbers:
    squares.append(number ** 2)

print(squares)

# shorter version of above
numbers2 = [1, 2, 3, 4, 5, 6]

# Comprehensions have two parts the iteration and the expression

#          | Expression |     Iteration      |
squares2 = [number ** 2 for number in numbers]  # list comprehension
squares3 = {number ** 2 for number in numbers}  # set comprehension
print(squares2)
print(squares3)

# another way to do the above
squares4 = [number ** 2 for number in range(1, 7)]
print(squares4)

