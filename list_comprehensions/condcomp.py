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

meals = []
for meal in menu:
    if "spam" not in meal:
        meals.append(meal)
print(meals)

print("*" * 80)
meals = [meal                                               # expression
         for meal in menu                                   # iterator
         if "spam" not in meal and "chicken" not in meal]   # filter(s)
print(meals)


fussy_meals = [meal                                     # expression
               for meal in menu                         # iterator
               if "spam" in meal or "eggs" in meal if not ("bacon" in meal and "sausage" in meal)  # filters
               ]
print(fussy_meals)

# else in comprehension
meals2 = []
print("*" * 80)
meals2 = [meal                                          # expression
          if "spam" not in meal else " meal skipped"    # condition
          for meal in menu                              # iterator
          ]
print(meals2)

for x in range(1, 31):
    fizzBuzz = "fizz buzz" if x % 15 == 00 \
        else "fizz" if x % 3 == 0 \
        else "buzz" if x % 5 == 0 \
        else str(x)
    print(fizzBuzz)
