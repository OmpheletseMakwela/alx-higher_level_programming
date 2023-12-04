#!/usr/bin/python3

def no_c(my_string):
    char_to_remove = 'cC'
    for char in char_to_remove:
        my_string = my_string.replace('c', '')
        my_string = my_string.replace('C', '')
        return my_string
