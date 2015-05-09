import stack
import person

s = stack.Stack()
for i in range(1, 10):
    temp_name = "rydge" + str(i);
    temp_person = person.Person(temp_name, 'male', str(i));
    s.join(temp_person);
s.showS();

while s.slength > 3:
    print("the person leaving from the stack is: " + s.leave().my_name);
s.showS();
