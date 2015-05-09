while True:
    print('please input your data:');
    userNums = input();
    if userNums == ".":
        break;
    userNums = userNums.split();
    print(userNums);
    userNums = [int(i) for i in userNums];
    for userNum in userNums:
        if userNum % 3 == 0 and userNum % 5 == 0:
            print('FizzBuzz');
        elif userNum % 3 == 0:
            print('Fizz');
        elif userNum % 5 == 0:
            print('Buzz');
        else:
            print(userNum);

