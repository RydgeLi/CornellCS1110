class OddError(Exception) :
    def __init__(self, value) :
        self.value = value
        
    def __str__(self) :
        return repr(self.value)
    
print("starting to do stuff ... please enter a number")

input_string = input()

try:
    n = int ( input_string )
    if n%2 == 1 :
        raise OddError(n)
    print("You entered an even integer")
except OddError as oe :
    print ("An odd error happened, with value = ", oe.value)
except (IOError, ValueError) :
    print("Oops ....")
    
all_numbers = []
all_words = []
all_puncts = []
flag = True
other_flag = True # used for continuing to read local data
try:
    data = open('amazing.txt')
    info = data.readline()
    if info == "":
        flag = False
    while flag is True: # so we're still reading data
        print("in while loop with info = " + info)
        if info == "NUMBERS\n":
            print("\treading numbers ...")
            info = data.readline()
            if info == "WORDS\n":
                other_flag = False
            while other_flag is True:
                all_numbers.append(info) # appending a number
                info = data.readline()
                if info == "WORDS\n":
                    other_flag = False
                    print("value of info should be WORDS, but = "+ info)
            # end while loop reading numbers
        print("finished reading numbers")
        other_flag = True # resetting the local reading flag
        
        if info == "WORDS\n":
            print("\treading words ...")
            info = data.readline()
            if info == "PUNCTS\n":
                other_flag = False
            while other_flag is True:
                all_words.append(info) # appending a word
                info = data.readline()
                if info == "PUNCTS\n":
                    other_flag = False
            # end while loop reading words
        print("finished reading numbers")
        other_flag = True # resetting the local reading flag
        
        if info == "PUNCTS\n":
            print("\treading punctuation ...")
            info = data.readline()
            if info == "":
                other_flag = False
            while other_flag is True:
                all_puncts.append(info) # appending a word
                info = data.readline()
                if info == "":
                    other_flag = False
            # end while loop reading puncts
        
        
        if info == "": # checks to see that it's read everything in the file
            flag = False
        # end if statement
    # end while loop reading the file
    for thingy in all_numbers:
        print(thingy)
    for thingy in all_words:
        print(thingy)
    for thingy in all_puncts:
        print(thingy)

except FileNotFoundError as err:
    print("File wasn't found -- sorry!!", err)

