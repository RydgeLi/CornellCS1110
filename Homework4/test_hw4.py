import class_tree, class_person
############################### you can change the data in "input.txt" to test my program! ####################

# define a exception to handle the case that an integer happens to be negative or zero
class OddError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

# test starts here
heights = []  # used to store all the height data from file
people = []  # a list to store all the Person objects
try:
    my_file = open('input.txt', 'r')
    temp = my_file.read()
    heights = temp.split()
    for i in range(len(heights)):
        if int(heights[i]) <= 0:
            raise OddError(heights[i])
        # convert all the data(string) into integers
        heights[i] = int(heights[i])
    # define some people, give each Person a name, a unique ID, and height
    for i in range(len(heights)):
        people.append(class_person.Peroson('Lee_' + str(i), i + 1, heights[i]))
    # define a person tree here
    tree = class_tree.BinSearchTree()
    # begin to insert people
    for item in people:
        tree.insert(item)
    
    result = []  # used to store the result of output
    result = tree.start_output()
    # show the result
    for item in result:
        print(item)
        
except FileNotFoundError:
    print("Couldn't find that file!")
except ValueError:
    print("Couldn't covert  data to an integer!")
except OddError as err:  # handle the case that an integer happens to be negative or zero
    print("Numbers can't be negative or zero! THe bad number is " + err.value)
finally:
    print("Done!")
