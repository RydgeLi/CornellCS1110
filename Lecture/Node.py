class Nodey:
    '''This class builds nodes, each of which can hold data, and a left and a right (meant to be themselves nodes)'''
    
    def __init__(self):
        self.data = None
        self.left = None
        self.right = None
        self.parent = None
        
    def set_data(self, stuff):
        self.data = stuff
        
    def get_data(self):
        return self.data
    
    def set_left(self, lefty):
        self.left = lefty
        
    def get_left(self):
        return self.left
    
    def set_right(self, righty):
        self.right = righty
        
    def get_right(self):
        return self.right
    
    def set_parent(self, part):
        self.parent = part
        
    def get_parent(self):
        return self.parent
    