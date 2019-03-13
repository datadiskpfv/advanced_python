from data import basic_plants_list, plants_list

print(plants_list[0])

# for plant in basic_plants_list:
#     print(plant[0])

print("-" * 30)

for plant in plants_list:
    print(plant.name, plant[1])

print("-" * 30)

example = plants_list[0]
print(example)

example = example._replace(lifecycle='Annual')
print(example)

print("-" * 30)

plants_list[0]._replace(lifecycle='Annual')     # named tuples are immutable
print(plants_list[0])
