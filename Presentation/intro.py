# # # Basics
# # print("Hello World! Anyone alive?")
# # print("please input an integer")
# # response_1 = input()
# # print("please input another integer")
# # response_2 = input()
# # arith = int(response_1) * int(response_2)
# # print("The product of " + response_1 + " and " + response_2 + " is ", arith)
# # 
# # 
# # # Control
# # if arith > 20:
# #     print("You are not alone!")
# # else:
# #     print("let's find more people")
# #       
# # number = 0
# # while number < arith:
# #     print('LOL')
# #     number = number + 1
# #      
# # for x in range(arith):
# #     print("Here!")
# # # 
# # 
# # Sequences
# name = "rydge"
# print(name * 3)
# print(name[1:-1])
# print(name + "li")
# print(name.replace('y', '###'))
#  
# tup = (1, 2, 3, 4, 5)
# print(tup)
# # tup[1] = 0
# lis = [1, 2, 3, 4, 5]
# print(lis)
# lis[1] = 0
#  
#  
# # tuple and list
# a = 1
# b = 2
# c = 3
# d = 4
# x = 5
# y = 6
# z = 7
# stuff = [a, b, c, d]
# print (stuff)
# print (stuff[0:3])
#  
# stuff[0:1] = [x, y, z]
# print (stuff)
#  
# for thing in stuff:
#     print ('thing is', thing)
#      
# file
my_file = open('amazing.txt', 'r+')
number_list = [];
for line in my_file:
    number_list.append(line);
print(number_list);
my_file.close();