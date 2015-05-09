while True:
    print('Please enter your numbers:(enter . to exit)');
    userNums = input();
    # users can stop the program by entering the '.'
    if(userNums == '.'):
        break;
    # convert the string to list
    userNums = userNums.split();
    userNums = [int(i) for i in userNums];
    # set the initial value of max_number,min_number,mean.
    max_number = userNums[0];
    min_number = userNums[0];
    mean = 0;
    for i in range(len(userNums)):
        # use the built-in functions: max and min instead of doing it myself.
        max_number = max(max_number, userNums[i]);
        min_number = min(min_number, userNums[i]);
        mean = mean + userNums[i];
    mean = mean / (i + 1);
    print('the MAX number is', max_number);
    print('the MIN number is ', min_number);
    print('the MEAN is ', mean);
    
print('You just ended the Program!')
