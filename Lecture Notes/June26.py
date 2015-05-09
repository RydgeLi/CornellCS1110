integ = "3aaaa72hhhh19jjjjdce"
isAnInteger = True
badstuff = ''
Digits = "0 1 2 3 4 5 6 7 8 9"
thedigit = Digits.split()
print(thedigit)

i = 0
while i in range(len(integ)):  # and isAnInteger:
    test = integ[i]
    if(test not in thedigit):
        if(test not in badstuff):
            badstuff = badstuff + test
        isAnInteger = False
    i = i + 1

if(isAnInteger):
    print('It is an integer')
else:
    print('Bad Stuff:' + badstuff)

            

    
    
