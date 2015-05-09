import node

class BinSearchTree:
    def __init__(self):
        self.root = None;
        self.size = 0
    
    def getSize(self):
        return self.size;
    
    def isEmpty(self):
        return self.size == 0
    
    def insert(self, data):
        if self.isEmpty():
            self.root = node.Node()
            self.root.set_data(data)
        else:
            self.insert_at_node(data, self.root)
        self.size = self.size + 1
            
    def insert_at_node(self, data, node):
        if data < node.get_data():
            if node.get_left() == None:
                temp = node.Node();
                temp.set_data(data);
                node.set_left(temp);
            else:
                self.insert_at_node(data, node.get_left());
        else:
            if node.get_right() == None:
                temp = node.Node();
                temp.set_data(data);
                node.set_right(temp);
            else:
                self.insert_at_node(data, node.get_right())
    
    
