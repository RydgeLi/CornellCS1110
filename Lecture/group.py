import population_builder

chris = population_builder.Person("Chrisy", "muddled", 98)

def random_name():
    vowels = "aeiouy"
    consonants = "bcdfghjklmnpqrstvwxz"
    return "Fred_"

people = []
for i in range(0,10000000):
    temp_name = random_name() + str(i)
    temp_person = population_builder.Person(temp_name, "wiggle", (10 + (i)//10)%55)
    people.append(temp_person)

print ("people have been built!")

def find(where, hunted): # where = list of things to look in, hunted = age hunted for
    found = False
    found_people = []
    for stuff in where:
        if stuff.my_age == hunted:
            found = True
            found_people.append(stuff);
    if not found:
        return None
    else:
        return found_people

'''for folk in find(people, 7):
    print(folk.all_info())'''