menu = [
    ["egg", "spam", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
    ["spam", "egg", "sausage", "spam"],
    ["chicken", "chips"]
]

# Use for loop to filter
for meal in menu:
    if "spam" not in meal:
        print(meal)

print("-" * 40)

# Use a comprehension to filter
meals = [meal for meal in menu if "spam" not in meal]
print(meals)

print("-" * 40)


# Use a filter method
def not_spam(meal_list: list):
    return "spam" not in meal_list


spamless_meals = list(filter(not_spam, menu))
print(spamless_meals)
