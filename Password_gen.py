# Mini Project - Random Password Generator

# Importing the relevant modules
import string
import random

# assigning values to variables
flag = 0
size = 0
uppercase_string = string.ascii_uppercase
lowercase_string = string.ascii_lowercase
punctuation_string = string.punctuation
numbers_string = string.digits
whitespaces_string = "   "
uppercase_flag = 0
lowercase_flag = 0
punctuation_flag = 0
numbers_flag = 0
whitespaces_flag = 0
count = 0

# creating lists
flag_list = [uppercase_flag, lowercase_flag, punctuation_flag, numbers_flag, whitespaces_flag]
string_list = [uppercase_string, lowercase_string, punctuation_string, numbers_string, whitespaces_string]
flag_name = ["uppercase", "lowercase", "punctuation", "numbers", "whitespaces"]

# Asking for the size of password
while flag == 0:
    i = input("Enter the size of password\n")
    try:
        size = int(i)
        flag = 1
    except:
        print("Please, enter a digit")

# Asking for conditions on the password
for index in range(0, 5):
    flag = 0
    while flag == 0:
        flag_list[index] = input("Do you want {} letters in password\n".format(flag_name[index]))
        if flag_list[index] == 'Y' or 'N':
            flag = 1
        else:
            print("Please, enter a valid option")
        if flag_list[index] == 'Y':
            count += 1

password = ""
case_count = size // count

# processing the password
for index in range(0, 5):
    if flag_list[index] == 'Y':
        for i in range(0, random.randint(1, case_count)):
            digit = list(string_list[index])[random.randint(0, len(list(string_list[index]))-1)]
            password = str(password) + str(digit)

remaining = size - len(password)
for i in range(0, remaining):
    password = str(password) + chr(random.randint(33, 126))

password_list = list(password)
random.shuffle(password_list)

# printing the password
print("Your password is: ")
print("".join(password_list[0: size]))
