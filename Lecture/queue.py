######import population_builder

class Queue:
    def join(self, p): # note that p is the thing being added
        self.storage.append(p)
        self.qlength = self.qlength + 1
    
    def leave(self):
        if self.isEmpty():
            return None
        temp = self.storage[self.front]
        self.front = self.front + 1
        self.qlength = self.qlength - 1
        return temp # thus returning the thing at the front 
        
    def isEmpty(self):
        return self.qlength == 0
    
    def showQ(self):
        tutti = ""
        for i in range(self.front, self.front + self.qlength):
            tutti = tutti + self.storage[i].my_name + ", " # assuming here that the thing is a person!!!
        return tutti
    
    def __init__(self) :
        self.storage = [] # to store people!!
        self.qlength = 0 # to hold the current number of things in the queue
        self.front = 0
        
        
class Stack:
    def join(self, p): # note that p is the thing being added
        self.storage.append(p)
        self.top = self.top + 1
        self.qlength = self.qlength + 1
    
    def leave(self):
        if self.isEmpty():
            return None
        temp = self.storage[self.top]
        self.top = self.top - 1
        self.qlength = self.qlength - 1
        return temp # thus returning the thing at the front 
        
    def isEmpty(self):
        return self.qlength == 0
    
    def showQ(self):
        if self.isEmpty():
            return "Im empty"
        tutti = ""
        for i in range(0, self.qlength):
            tutti = tutti + self.storage[i].my_name + ", " # assuming here that the thing is a person!!!
        return tutti
    
    def __init__(self) :
        self.storage = [] # to store people!!
        self.qlength = 0 # to hold the current number of things in the queue
        self.top = -1