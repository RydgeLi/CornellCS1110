integ = "37twttwitw219"
isAnInteger = True
badstuff = "" # a string to hold all the bad content
#digits = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")
Digits = "0 1 2 3 4 5 6 7 8 9"
theDigits = Digits.split()
print(theDigits)


i = 0
while i in range(len(integ)) : # and isAnInteger :
    test = integ[i]
    if test not in theDigits :
        #print("an interloper appeared")
        if test not in badstuff :
            badstuff = badstuff + test
        isAnInteger = False
    i = i + 1

if isAnInteger :
    print("The supposed integer was indeed an integer.")
else :
    print("The supposed integer failed to be an integer!!  The bad stuff was ... " + badstuff)