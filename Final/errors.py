class nonPositive(Exception): # raise this error if the input for measure number is non positive
    def __init__(self,value):
        self.value = value
    def __str__(self) :
        return repr(self.value)