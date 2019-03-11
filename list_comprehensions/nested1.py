burgers = ["beef", "chicken", "spicy bean"]
toppings = ["cheese", "egg", "beans", "spam"]

# burgers will be the first iterator then toppings
for meals in [(burger, topping) for burger in burgers for topping in toppings]:
    print(meals)

print()

# for burger in burgers:
#     for topping in toppings:
#         print((burger, topping))

# the outer iterator will run first, in this case toppings then burgers
for nested_meals in [[(burger, topping) for burger in burgers] for topping in toppings]:
    print(nested_meals)

print()

# the outer iterator will run first, in this case burgers then toppings
for nested_meals in [[(burger, topping) for topping in toppings] for burger in burgers]:
    print(nested_meals)
