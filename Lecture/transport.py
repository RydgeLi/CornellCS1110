class Vehicle:
    def __init__(self, people=[], things=[]):
        self.people = people  # people will be constructed via the Gens class
        self.things = things
        self.owner = "Them"
        
    def set_owner(self, owner):
        self.owner = owner
        
    def info(self):
        temp = 'The people in my vehicle are:\n\t'
        for folk in self.people:
            temp = temp + folk.info() + ', '
        temp = temp + '\nand the things are:\n\t'
        for stuff in self.things:
            temp = temp + stuff.info() + ', '
        return temp
    
class Car(Vehicle):
    def __init__(self, people=[], things=[], fuel_type='petrol', max_seats=4):
        super(Car, self).__init__(people, things)
        self.engine_fuel = fuel_type
        self.max_seats = max_seats  # # could have fun controlling the seat occupants ....
        
    def info(self):
        temp = super(Car, self).info()
        temp = temp + '\n\t\tusing fuel type = ' + self.engine_fuel
        temp = temp + ', and having ' + str(self.max_seats) + ' seats.'
        return temp
        
class Bike(Vehicle):
    def __init__(self, number_gears=1):
        self.number_gears = number_gears
        
