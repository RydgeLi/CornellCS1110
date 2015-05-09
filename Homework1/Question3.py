# input like this:
# I am Yujie Li.
# What is your name?
# 0
import string;
end = '0';
# exclude contains all the punctuation.
exclude = set(string.punctuation);
while True:
    # user_input is the raw string that user entered.
    user_input = "";
    # user_string is the string without all the punctuation. 
    user_string = "";
    # result_list contains all the unique words.
    result_list = [];
    print('Please enter your text:(enter 0 for a new line to end your input)');
    buffer = input();
    while buffer != end:
        user_input = user_input + buffer;
        buffer = input();
    # begin to replace all the punctuation with space except the hyphens.
    for ch in user_input:
        if ch in exclude:
            if ch != '-':
                user_string = user_string + ' ';
        else:
            user_string = user_string + ch;
    # change the string to list.
    user_string = user_string.split();
    # begin to storage all the unique words into result_list.
    for item in user_string:
        if item not in result_list:
            result_list.append(item);
    # print the number of unique words
    print("The Number of the words is: ", len(result_list));
    print("The list is: ", result_list);
