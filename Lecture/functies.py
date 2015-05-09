def print_squares(a=1,b=10) :
    '''Print squares from a to b inclusively'''
    for n in range(a, b+1) :
        print(str(n*n) + ", ")
        
def get_int_from_keyboard() :
    print("please enter an integer")
    str_input = input()
    return int(str_input)

