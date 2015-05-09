import person
fred=person.Person('Fred','efefefe',167);
#  
# zark=person.Person('zark','male',7);
#  
# zark.add_friend(fred);
# zark.show_friedns();
# zark.list_friends();

people_list=[]
people_list.append(fred);
for i in range(1,100):
    people_list.append(person.Person('No.'+str(i),'male',i));
    
# print(people_list[2]);
# print(people_list[2].all_info());

# for folk in people_list:
#     print(folk.all_info())

def find(where,target):
    found=False;
    for stuff in where:
        if stuff==target:
            found=True;
    return found;

print(find(people_list,fred));
