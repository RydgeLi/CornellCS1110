class Peroson:
    def __init__(self, name, number, height):
        self.name = name
        self.id = number  # unique ID number
        self.height = height  # the height data read from file
# set and get functions
    def set_height(self, height):
        self.height = height
        
    def get_height(self):
        return self.height
    
    def get_name(self):
        return self.name
    
    def get_id(self):
        return self.id
# return  all the information of this Person including "name","ID", and "Height"
    def get_info(self):
        return 'name: ' + self.name + ', ID is ' + str(self.get_id()) + ', and Height: ' + str(self.height) + ' cm'
