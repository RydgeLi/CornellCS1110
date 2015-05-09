# things: name, price and any other things
# for things:
# change price
class thing:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        
    def info(self):
        print('thing name:', self.name, 'thing price:', self.price)
        
    def change_price(self, changed_price):
        self.price = changed_price
