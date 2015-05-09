class Person:
    '''This class will allow me to make people!
    object attributes:my_name, my_gender,my_age,my_frineds'''
    
    def person_kind(self):
        if self.my_gender[0] == 'm':return 'lad'
        elif self.my_gender[0] == 'f':return 'lass'
        else:return 'martian';
        
    def all_info(self):
        return "name:" + self.my_name + ", age:" + str(self.my_age) + ", kind:" + self.person_kind();
        
    def add_friend(self, nice_person):
        self.my_friends.append(nice_person);
    
    def show_friedns(self):
        print(self.my_friends);
    
    def list_friends(self):
        if(len(self.my_friends) == 0):
            all_friends = "I have no friends :(";
        else:
            all_friends = "my friends: "
            for friend in self.my_friends:
                all_friends = all_friends + friend.all_info();
        print(all_friends);
    
    def __init__(self, name, gender, age):
        self.my_name = name;
        self.my_gender = gender;
        self.my_age = age;
        self.my_friends = [];
