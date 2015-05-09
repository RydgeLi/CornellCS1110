# Bank Account: name, id number, balance
# for bank account:
# change balance
class account:
    def __init__(self, name, number, balance):
        self.name = name
        self.number = number
        self.balance = balance
    
    def info(self):
        print('account number:', self.number, 'account name:', self.name, 'account balance:', self.balance)
        
    def change_balance(self, changed_balance):
        self.balance = changed_balance
        
    def add_money(self, money):
        self.balance = self.balance + money
        print('added', money, 'to the', self.name, 'account')
    
    def spend_money(self, money):
        self.balance = self.balance - money
        print('spent', money, 'from the', self.name, 'account')
