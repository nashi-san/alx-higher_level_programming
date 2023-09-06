#!/usr/bin/python3
def remove_char_at(str, n):
    output_str = ""
    for i, c in enumerate(str):
        if i != n:
            output_str += c
    return output_str
