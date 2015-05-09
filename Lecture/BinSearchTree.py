import Node

class BinSearchTree:
    def __init__(self):
        self.root = None # to hold the root node
        self.size = 0 # to give the number of terms in the tree
        
    def getSize(self):
        return self.size
    
    def isEmpty(self):
        return self.size == 0
    
    def insert(self, data):
        if self.isEmpty():
            self.root = Node.Nodey()
            self.root.set_data(data)
        else:
            self.insert_at_node(data, self.root)
        self.size = self.size + 1
        
    def insert_at_node(self, data, node):
        if data.lessThan(node.get_data()):
            print("going left")
            if node.get_left() == None:
                temp = Node.Nodey()
                temp.set_data(data)
                node.set_left(temp)
            else:
                self.insert_at_node(data, node.get_left())
        else:
            print("going right")
            if node.get_right() == None:
                temp = Node.Nodey()
                temp.set_data(data)
                node.set_right(temp)
            else:
                self.insert_at_node(data, node.get_right())
                
    def printLR(self):
        self.printLRnodal(self.root)
        
    def printLRnodal(self, node):
        if node.get_left() != None:
            self.printLRnodal(node.get_left())
        print(node.get_data().info() + ', ')
        if node.get_right() != None:
            self.printLRnodal(node.get_right())
    