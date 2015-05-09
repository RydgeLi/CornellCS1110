import node;

class Tree:
    def __init__(self):
        self.root = None;
        self.size = 0; # the number of things in the tree
    
    def get_size(self):
        return self.size;
    
    def Linsert(self,data,given_node,side):
        '''insert data to the left side of the given node'''
        temp_node = node.Node();
        temp_node.set_data(data);
        old_left = given_node.get_left();
        given_node.set_left(temp_node);
        if side=="left":
            temp_node.set_left(old_left);
        else:
            temp_node.set_right(old_left);    
        self.size =self.size+1;
    
    def Rinsert(self,data,given_node,side):
        '''insert data to the right side of the given node'''
        temp_node = node.Node();
        temp_node.set_data(data);
        old_right = given_node.get_right();
        given_node.set_right(temp_node);
        if side=="right":
            temp_node.set_right(old_right);
        else:
            temp_node.set_left(old_right);
        temp_node.set_right(old_right); 
        self.size =self.size+1;
        
    def isEmpty(self):
        return self.size==0;
    
    def insert_by_bigness(self,data):
        temp_node=node.Node();
        temp_node.set_data(data);
        if self.isEmpty():
            self.root=temp_node;
        else:
            print("still hunting");
#             self.insert_by_bigness_locally(data, self.root);
        self.size=self.size+1;
    
    def insert_by_bigness_locally(self,data,given_node):
        temp_node=node.Node();
        temp_node.set_data(data);
        if data < given_node:
            print('go left');
            if given_node.get_left() == None:
                given_node.set_left(temp_node);
            else:
                self.insert_by_bigness_locally(data, given_node.get_left());
        if data > given_node:
            print('go right');
            if given_node.get_right() == None:
                given_node.set_right(temp_node);
            else:
                self.insert_by_bigness_locally(data, given_node.get_right());
    
    
            
            
            
            
            
        