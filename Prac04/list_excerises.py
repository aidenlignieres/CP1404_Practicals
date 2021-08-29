"""
A program which requires 5 numbers from user
and is inputed into a list then will print
some key information about the list
examples: max, min, sum, len, average
"""

# basic list operations
user_input = 0
number_list = []

while user_input != 5:
    user_input += 1
    number = int(input("Number: "))
    number_list.append(number)

# print(number_list)
print("The first number is {}".format(number_list[0]))
print("The last number is {}".format(number_list[-1]))
print("The smallest number is {}".format(min(number_list)))
print("The biggest number is {}".format(max(number_list)))
print("The average of the numbers is {}".format(sum(number_list) / len(number_list)))

# woefully inadequate security checker
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

user_name = input("Please enter your username: ")
if user_name in usernames:
    print("Access Granted")
else:
    print("Access denied")

