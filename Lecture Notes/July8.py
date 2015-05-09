class oddError(Exception):
    def __init__(self, value):
        self.value = value;
        
    def __str__(self):
        return repr(self.value);
    
print('starting to do stuff');
print('input a number:');
input_string = input();
print(input_string);

try:
    n = int(input_string);
    if n % 2 == 1:
        raise oddError(n);
    print('you entered a even number');

except oddError as oe:
    print('An odd error happened, with value = ', oe.value);
    
except(IOError, ValueError):
    print('Oops...');

#############################################################################################################################

all_data = [];
flag = True;

try:
    data = open("my_file.txt");
    info = data.readline();
    if info == "":
        flag = False;
    while flag:
        print('in while loop, info: ' + info);
        all_data.append(info);
        info = data.readline();
        if info == "":
            flag = False;
        
except FileNotFoundError as err:
    print("file wasn't found....sorry", err);
    print(info);
