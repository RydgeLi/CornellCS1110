class Queue:
	"""doc string for Queue"""
	def __init__(self):
		self.storage = [];  # to store person
		self.qlength = 0;
		self.front = 0;

	def join(self, person):
		self.storage.append(person);
		self.qlength = self.qlength + 1;

	def leave(self):
		p = self.storage[self.front];
		self.front = self.front + 1;
		self.qlength = self.qlength - 1;
		return p;

	def isEmpty(self):
		return self.qlength == 0;

	def showQ(self):
		for i in range(self.front, self.front + self.qlength):
			print(self.storage[i].my_name);




		
