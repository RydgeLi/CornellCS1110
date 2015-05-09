#-------------------------------------------------------------------------------
# Andrea Dietrich
# Homework 2
#-------------------------------------------------------------------------------
class Person:

    def __init__(self, name = "me", stuff = []):
        self.my_name = name
        self.my_stuff = stuff

    def random_name(self): #this method creates a random name for a person
        import random
        vowels = "aeiouy" #the vowels
        consonants = "bcdfghjklmnpqrstvwxy" #the consonants
        length = random.randrange(3,6) #creating a name between 3 and 6 letters long
        letter = "" #empty string to hold a random letter
        letter = consonants[random.randrange(0,19)] #all names start with consonants
        name = "" #empty string to hold the name
        name = name + letter #appending the first letter to the name
        for i in range (length): #loop through the random name length
            if letter in consonants: #if the letter is a consonant
                letter = vowels[random.randrange(0,6)]#the next letter is a vowel
            else :
                letter = consonants[random.randrange(0,19)] #if the letter is a vowel, the next letter is a consonant
            name = name + letter #add the letter to the name
        capname = name.capitalize() #capitalize the name
        return capname #return the capitalized name

    def random_stuff(self): #this method grabs a collection of items for a person to own
        import Stuff
        all_my_stuff = Stuff.Item().collection()
        return all_my_stuff

    def open_account(self): #this method opens a bank account for a person. It defaults to a $200 balance.
        import Accounts
        accnum = 0
        amount = 200
        bank = Banks.Bank("First Bank")
        account = Accounts.Account(accnum, amount, person, )
        return account