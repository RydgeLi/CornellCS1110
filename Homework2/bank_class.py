# Bank: name, id number, list of counts
# for Bank:
# add account to list
class bank:
    def __init__(self, name, list_of_accounts):
        self.name = name
        self.list_of_accounts = list_of_accounts
    
    def show_accounts(self):
        print('Here is', self.name, 'info:')
        for item in self.list_of_accounts:
            item.info()
            print('--------------------')
        
    def add_accounts(self, account):
        isExisted = False
        for item in self.list_of_accounts:
            if item == account:
                isExisted = True
                print('We already had the account')
        if isExisted == False:
            self.list_of_accounts.append(account)
            
    def del_account(self, account):
        isDeleted = False
        for item in self.list_of_accounts:
            if item == account:
                self.list_of_accounts.remove(item)
                isDeleted = True
        if isDeleted == False:
            print("The account you want to delete doesn't exist")
