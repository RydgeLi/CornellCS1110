# this Node class is used to hold Person objects
class Node:
    def __init__(self, data):
        # data, left, and right are all Persons
        self.data = data
        self.left = None
        self.right = None
    
    # return the Person object
    def get_data(self):
        return self.data
    # get and set functions for left and right Person
    def get_left(self):
        return self.left
    
    def set_left(self, node):
        self.left = node;
    
    def get_right(self):
        return self.right
    
    def set_right(self, node):
        self.right = node
    
    # compare this Node's Person's height to the other Person's height
    # if this Node's Person's height is larger, return True
    def isLarger(self, other):
        if self.get_person_height() > other.get_height():
            return True
        return False
    
    # functions for getting this Node's Person's information including height and everything
    def get_person_height(self):
        return self.data.get_height()
    
    def get_person_info(self):
        return self.data.get_info()
    
