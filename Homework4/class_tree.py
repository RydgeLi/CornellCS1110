import class_node

class BinSearchTree:
    def __init__(self):
        self.root = None  # root of the tree
        self.size = 0  # numbers of nodes
        
    def get_size(self):
        return self.size
    
    # return True if this tree has zero nodes
    def isEmpty(self):
        return self.size == 0
    # start to insert a data(the data is a Person) arranged like a binary search tree via their height. 
    # if the tree is empty, put the data(Person) into a new Node and make it the root
    def insert(self, data):
        if self.isEmpty():
            self.root = class_node.Node(data)
        else:
            # while the tree is not empty, continue to insert the new data calling the "insert_at_node" function
            self.insert_at_node(data, self.root)
        self.size = self.size + 1
    
    # input the data(Person) and the given node(initially it's root)
    # using recursion here
    def insert_at_node(self, data, node):
        # if the  height of the given node(Person) is larger than that of new data(Person), put the data into it's left
        # if the node has no left, make the data it's left
        # else, continue to call the function
        if node.isLarger(data):
            if node.get_left() == None:
                temp = class_node.Node(data)
                node.set_left(temp)
            else:
                self.insert_at_node(data, node.get_left())
        # put the data into the node's right
        # if the node has no right, make the data it's right
        # else, continue to call the function
        else:
            if node.get_right() == None:
                temp = class_node.Node(data)
                node.set_right(temp)
            else:
                self.insert_at_node(data, node.get_right())
    
    # prepare to output the whole tree
    def start_output(self):
        if self.isEmpty():
            print("The tree is empty")
            return None
        else:
            print('This tree has ' + str(self.size) + ' Nodes:')
            print(" Following is all the nodes in ascending order")
            result_list = []  # a list to store all the nodes in ascending order
            self.output(self.root, result_list)  # call the "output" function to begin output
            return result_list  # return the ordered list
    
    # using recursion here
    # because it' in ascending order: we should output the tree like "left->self->right"
    def output(self, node, result_list):
        # first, left
        if node.get_left() != None:
            self.output(node.get_left(), result_list)
        # then, self
        result_list.append('\t' + node.get_person_info())
        # last, right
        if node.get_right() != None:
            self.output(node.get_right(), result_list)
        

