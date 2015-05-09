# person: name, list of things(including amount), bank & account number
class person:
    def __init__(self, name, list_of_things, bank, accounts):
        self.name = name
        self.list_of_things = list_of_things
        self.bank = bank
        self.accounts = accounts
        
    def show_list(self):
        print('Here is what', self.name, 'has:')
        for item in self.list_of_things:
            item[0].info()
            print('amount:', item[1])
        print('--------------------')
    
    def info(self):
        self.show_list()
        print('Here is', self.name, 'accounts:')
        for account in self.accounts:
            account.info()
        print('--------------------')
            
# for people:
# add and remove things
    def add_things(self, thing, option=1):
        isExisted = False;
        for item in self.list_of_things:
            if item[0] == thing:
                isExisted = True
                self.list_of_things.remove(item)
                self.list_of_things.append((thing, item[1] + option))
        if isExisted == False:
            self.list_of_things.append((thing, option))
        
    
    def remove_things(self, thing, option=1):
        if option == 'all':
            self.list_of_things.remove(thing)
        else:
            for item in self.list_of_things:
                if item[0] == thing:
                    if item[1] - option == 0:
                        self.list_of_things.remove(item)
                    else:
                        self.list_of_things.remove(item)
                        self.list_of_things.append((thing, item[1] - option))
