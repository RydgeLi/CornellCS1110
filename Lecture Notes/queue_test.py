import queue
import person

# queue test
q = queue.Queue();
for i in range(1, 10):
	temp_name = "rydge" + str(i);
	temp_person = person.Person(temp_name, 'male', str(i));
	q.join(temp_person);
q.showQ();

while q.qlength > 3:
	print("the person leaving from the queue is: " + q.leave().my_name);

q.showQ();
