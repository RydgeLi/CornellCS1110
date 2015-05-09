import population_builder
import queue

people = []
for i in range(0,1000):
    temp_name = "Fred_" + str(i)
    temp_person = population_builder.Person(temp_name, "wiggle", (10 + (i)//10)%55)
    people.append(temp_person)

s = queue.Stack() 
print ('The stack has length = ' + str(s.qlength) )

s.join(people[88])
print ('The queue has length = ' + str(s.qlength) )
s.join(people[276])
print ('The queue has length = ' + str(s.qlength) )
for i in range(100, 832, 75):
    s.join(people[i])
    
print ('The queue has length = ' + str(s.qlength) )

print(s.showQ())

while s.qlength > 4:
    print ('The following person has just left the queue: ' + s.leave().my_name)
    
    
print(s.showQ())