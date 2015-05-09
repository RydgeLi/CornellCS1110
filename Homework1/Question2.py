# input like this:
# aaabbbbbdddccccc
# ffffjddejndnjk
# 0
end = '0';
while True:
    print('please enter your text:(enter 0 for a new line to end your input)');
    user_input = "";
    buffer = input();
    while buffer != end:
        user_input = user_input + buffer;
        buffer = input();
    # delete all the space in the string user inputed
    user_input = ''.join(ch for ch in user_input if ch != ' ');
    # the list characters stores all the characters in user_input
    characters = [];
    # max_n used to store the count of the most common characters
    # max_c is a list used to store all the most common characters 
    max_n = 0;
    max_c = [];
    # min_n used to store the count of the least common characters
    # min_c is a list used to store all the least common characters 
    min_n = len(user_input);
    min_c = []
    # find all the characters in user_input
    for c in user_input:
        if c not in characters:
            characters.append(c);
    # count the frequency of occurrence of the most and the least common characters
    for item in characters:
        max_n = max(max_n, user_input.count(item));
        min_n = min(min_n, user_input.count(item));
    # using the max_n and min_n to find the most and the least common characters
    for item in characters:
        if user_input.count(item) == max_n and item not in max_c:
            max_c.append(item);
        if user_input.count(item) == min_n and item not in min_c:
            min_c.append(item);
    # print the result list.
    print('The most common characters are:');
    print(max_c);
    print('The least common characters are:');
    print(min_c);