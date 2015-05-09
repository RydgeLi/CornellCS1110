import Node

class tree:
    
    def __init__(self):
        self.root = None
        self.size = 0 # the number of things in the tree
        
    def get_size(self):
        return self.size
    
    def isEmpty(self):
        return self.size == 0
    
    def Linsert(self, data, node, side):
        '''this inserts data to the left of the given node, putting the old stuff to the given SIDE of this new node'''
        temp_node = Node.Nodey()
        temp_node.set_data(data) # so now have a temp node containing the desired data
        old_left = node.get_left() # so have a pointer to the stuff on the left of the given node
        node.set_left(temp_node) # so now have set this temp node to be the left node of the given node
        if side == "left":
            temp_node.set_left(old_left) # so now have re-attached the old left stuff to the left of the new node
        else :
            temp_node.set_right(old_left) # so now have re-attached the old left stuff to the right of the new node
        self.size = self.size + 1
        
    def Rinsert(self, data, node, side):
        '''this inserts data to the right of the given node, putting the old stuff to the given SIDE of this new node'''
        temp_node = Node.Nodey()
        temp_node.set_data(data) # so now have a temp node containing the desired data
        old_right = node.get_right() # so have a pointer to the stuff on the right of the given node
        node.set_right(temp_node) # so now have set this temp node to be the right node of the given node
        if side == "left":
            temp_node.set_left(old_right) # so now have re-attached the old right stuff to the left of the new node
        else :
            temp_node.set_right(old_right) # so now have re-attached the old left stuff to the right of the new node
        self.size = self.size + 1
        
    def insert_by_bigness(self, data):
        temp_node = Node.Nodey()
        temp_node.set_data(data)
        if self.isEmpty():
            self.root = temp_node
        else:
            print("still hunting")
        self.size = self.size + 1
        
    def insert_by_bigness_locally(self, data, node):
        ''' compares data with the data in the node and decides to go left or right'''
        if data < node.get_data():
            print("go left")
            if node.get_left() == None:
                node.set_left(Node.Nodey(data))
            else:
                self.insert_by_bigness_locally(data, node.get_left())
        else:
            print("go right")
            
        