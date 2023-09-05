#!/usr/bin/python3
for c in range(122, 96, -1):
    o = ""
    if c % 2 != 0:
        o = chr(c - 32)
    else:
        o = chr(c)
    print("{:s}".format(o), end='')
