#!/usr/bin/python3

def no_c(my_string):
    new_string = ""
    for idx, char in enumerate(my_string):
        if char in ['c', 'C']:
            new_string = my_string[:idx] + my_string[idx + 1:]
    
    return new_string
