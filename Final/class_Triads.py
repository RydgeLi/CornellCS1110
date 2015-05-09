class Triad:
    def __init__(self, root, third, fifth):  # root is the number of the root node
        self.root = root
        self.third = third
        self.fifth = fifth
        self.friend = None  # notes can make friends with each other!!
        self.notes = [self.root, self.third, self.fifth]
    
    def set_friend(self, friend):  # adds a friend triad that will be often used together
        self.friend = friend
        friend.friend = self
        
    def set_third(self, third):  # third is the number of the third note
        self.third = third
    
    def set_fifth(self, fifth):  # fifth is the number of the fifth note
        self.fifth = fifth
