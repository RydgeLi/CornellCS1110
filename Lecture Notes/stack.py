class Stack:		
	def __init__(self):
		self.storage = [];  # to store person
		self.slength = 0;
		self.top = -1;

	def join(self, person):
		self.storage.append(person);
		self.top = self.top + 1;
		self.slength = self.slength + 1;

	def leave(self):
		if self.isEmpty():
			return None;
		p = self.storage[self.top];
		self.top = self.top - 1;
		self.slength = self.slength - 1;
		return p;

	def isEmpty(self):
		return self.slength == 0;

	def showS(self):
		for i in range(0, self.slength):
			print(self.storage[i].my_name);
