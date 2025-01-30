#!/usr/bin/env python3
# Strings 1

str1 = 'Hello World!!'
str2 = 'Seneca College'

num1 = 1500
num2 = 1.50

def first_five(str):
    # Place code here - refer to function specifics in section below
    return str[0:5]

def last_seven(str):
    # Place code here - refer to function specifics in section below
    return str[-7:]

def middle_number(num):
    # Place code here - refer to function specifics in section below
    num_string = str(num)

    if "." in num_string: # Used to account for loss of trailing decimal '0s' in numbers 
        num_string += "0"
    
    middle_index = (len(num_string) // 2) - 1
    return num_string[middle_index : middle_index + 2]

def first_three_last_three(str1, str2):
    # Place code here - refer to function specifics in section below
    return str1[:3] + str2[-3:]


if __name__ == '__main__':
    print(first_five(str1))
    print(first_five(str2))
    print(last_seven(str1))
    print(last_seven(str2))
    print(middle_number(num1))
    print(middle_number(num2))
    print(first_three_last_three(str1, str2))
    print(first_three_last_three(str2, str1))