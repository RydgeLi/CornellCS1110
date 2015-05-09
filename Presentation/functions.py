def print_squares(a=1, b=10):
    '''Print squares from a to b inclusively'''
    for n in range(a, b + 1):
        print(str(n * n) + ',')
    
def get_int_form_keyboard():
    print('Please input an integer')
    str_input = input()
    return int(str_input)

def which_is_bigger():
    a = get_int_form_keyboard()
    b = get_int_form_keyboard()
    if a > b: return (str(a) + ' is bigger than ' + str(b))
    if a < b: return (str(b) + ' is bigger than ' + str(a))
    if a == b: return "they're the same"
