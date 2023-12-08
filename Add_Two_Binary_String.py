# -*- coding: utf-8 -*-
"""
Problem: Give a list of binary strings, return their sum as a binary string.

Algorithm:

1. We got all the strings, all of them are located at the representation where base is 2.
2. Convert all strings in base 2 into base 10 which is decimal representation.The length of binary string should be the same as the decimal list.
3. Sum over all the values in the representation of base 10.
4. We converted the sum which is at the representation of base 10 into binary representation to obtain final results.

"""

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
