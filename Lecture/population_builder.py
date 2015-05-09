class Person :
    '''This class builds people
    object attributes: my_name, my_gender, my_age, my_friends'''
    
    def most_info(self) :
        info = 'My name is ' + self.my_name
        info = info + ', and I\'m a ' + str(self.my_age) + ' year old ' + self.my_gender
        return info
        
    def all_info(self) :
        return self.most_info() + ', and ' + self.list_friends()
        
    def add_friend(self, thingy) :
        self.my_friends.append(thingy)
        
    def list_friends(self) :
        if len(self.my_friends) == 0 :
            all_friends = "I have no friends :("
        else :
            all_friends = "my friends will introduce themselves: "
            for friend in self.my_friends :
                all_friends = all_friends + '\n\t' +friend.most_info()
        return all_friends
    
    def __init__(self, name, gender, age) :
        self.my_name = name
        self.my_gender = gender
        self.my_age = age
        self.my_friends = []