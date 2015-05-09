import matrix

# function to read data from file
def read_from_file(filename):
    numbers = []
    my_file = open(filename, 'r')
    for line in my_file:
        temp_numbers = []
        temp_numbers = line.split()
        for i in range(len(temp_numbers)):
            temp_numbers[i] = float(temp_numbers[i])
        numbers.append(temp_numbers)
    return numbers

# read 4 sets of data from files
numbers1 = read_from_file('input1.txt')
numbers2 = read_from_file("input2.txt")
numbers3 = read_from_file('multiply_input1.txt')
numbers4 = read_from_file("multiply_input2.txt")

# define 4 matrixes
m1 = matrix.Matrix()
m2 = matrix.Matrix()
m3 = matrix.Matrix()
m4 = matrix.Matrix()
# put data into each matrix
m1.build_matrix(numbers1)
m2.build_matrix(numbers2)
m3.build_matrix(numbers3)
m4.build_matrix(numbers4)
# show all the matrixes
print("****************m1 matrix:****************")
m1.show_matrix()
print("****************m2 matrix:****************")
m2.show_matrix()
print("****************m3 matrix:****************")
m3.show_matrix()
print("****************m4 matrix:****************")
m4.show_matrix()
# perform addition of m1 and m2
if m1.add(m2):
    print("****************After m1 adds m2:****************")
    m1.show_matrix()
 
# perform subtracting of m2 and m1
if m2.substract(m1):
    print("****************After m2 subtracts m1:****************")
    m2.show_matrix()
 
# perform multiplying 
mul_result = m3.multiply(m4)
if mul_result:
    print('****************the result of multiplying is:****************')
    for row in mul_result:
        print(row)
