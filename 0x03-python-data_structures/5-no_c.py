#!/usr/bin/python3
def no_c(my_string):
    new_str = ""
    for cr in range(len(my_string)):
        if (my_string[cr] != 'c' and my_string[cr] != 'C'):
            new_str += my_string[cr]
    return new_str
