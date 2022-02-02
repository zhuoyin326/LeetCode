# -*- coding: utf-8 -*-
"""
Created on Sat Jan 15 21:44:31 2022

@author: zhuo
"""

"""Joe's code"""

binary_string_list = ["11", "1", "1010", "1011"]
print(len(binary_string_list))

decimal_integer_list = [0]*len(binary_string_list)
print(decimal_integer_list)

def sum_strings(binary_string_list):
    decimal_integer_list = binary_to_integer(binary_string_list)
    string_c = bin(sum(decimal_integer_list))
    output_string_c = string_c [2:]
    return output_string_c

def binary_to_integer(binary_string_list):
    decimal_integer_list = [0]*len(binary_string_list)
    print(decimal_integer_list)
    for i in range(len(binary_string_list)):
        print(i)
        decimal_integer_list[i] = int(binary_string_list[i], 2)
    print(decimal_integer_list)
    return decimal_integer_list

print(sum_strings( ["11", "1", "1010", "1011"]))
