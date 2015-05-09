print('June 24')
total = 0
base_value = 3
power = 100
number_of_time = 0

for number in range(power):
    total = total + 1
print('the total is ' + str(total))

while number_of_time < power:
    total = total + base_value
    number_of_time = number_of_time + 1

print('the total is ' + str(total))

for x in range(1, power + 1):
    total = total + 1

for i in range(-8, -23, -1):
    print('i->' + str(i))

print('the total is ' + str(total))

test = 'hello world'
print(test[1:-2])
print(test[-2:1])
print(test.capitalize())

print(test.replace('h', 'rydg'))
