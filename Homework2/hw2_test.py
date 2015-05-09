import person_class
import thing_class
import bank_class
import account_class

#-----------------functions to perform a transaction---------------------------
# find things
def find_things(target, list_of_things):
    for item in list_of_things:
        if item[0] == target:
            return True
    return False

# def find_account(target,bank):
#     status=False;
#     index=0;
#     for i in range(len(bank.list_of_accounts)):
#         if bank.list_of_accounts[i]==target:
#             status=True;
#             index=i;
#     if status:
#         return index;
#     else:
#         return None;

# check balance before a transaction
def check_balance(owner, cost):
    status = False
    index = 0
    for i in range(len(owner.accounts)):
        if owner.accounts[i].balance >= cost:
            status = True
            index = i
    if status:
        return index
    else:
        return None

# performing a transaction
def transaction(buyer, seller, thing, amount=1):
    if find_things(thing, seller.list_of_things):
        result = check_balance(buyer, thing.price * amount)
        if result != None:
            print('now performing a transaction')
            buyer.accounts[result].spend_money(thing.price * amount)
            buyer.add_things(thing, amount)
            seller.remove_things(thing, amount)
            seller.accounts[0].add_money(thing.price * amount)
            print('success!')       
        else:
            print('failed! Please check your account balance!')
    else:
        print("the seller doesn't have the thing that buyer needs!")


#--------------------------test starts here:---------------------------------
# set up banks:
bank1 = bank_class.bank('bank1', [])
bank2 = bank_class.bank('bank2', [])
# set up accounts:
account1 = account_class.account('Visa', 1234, 0)
account2 = account_class.account('MasterCard', 5678, 0)
account3 = account_class.account('Express', 8888, 0)
# add accounts to banks:
bank1.add_accounts(account1)
bank1.add_accounts(account3)
bank2.add_accounts(account2)
# show banks info:
# bank1.show_accounts()
# bank2.show_accounts()

# set up things:
iphone = thing_class.thing('iPhone 5s', 600)
ipad = thing_class.thing('iPad Air', 500)

# set up people:
rydge = person_class.person('rydge', [(iphone, 1)], [bank1], bank1.list_of_accounts)
christina = person_class.person('christina', [(ipad, 1)], [bank2], bank2.list_of_accounts)
rydge.info()
christina.info()

# perform a transaction which will fail because of the balance
transaction(rydge, christina, ipad)

# add balance to the account
rydge.accounts[0].add_money(500)

# perform a transaction again
transaction(rydge, christina, ipad)
# show the info after the transaction
rydge.info()
christina.info()
