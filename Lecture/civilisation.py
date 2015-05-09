import population_builder

fred = population_builder.Person('Fred', 'male', 167)
chris = population_builder.Person('chris', 'venusian', 30)
chrisy = population_builder.Person('chris', 'funny', 90)

print(fred.all_info())

fred.add_friend(chris)
fred.add_friend(chrisy)
chris.add_friend(fred)

print(fred.all_info())