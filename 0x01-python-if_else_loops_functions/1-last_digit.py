#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastdigit = str(number)[-1]
if number < 0:
    lastdigit = "-" + lastdigit
if int(lastdigit) > 5:
    print(f"Last digit of {number} is {lastdigit} and is greater than 5")
elif int(lastdigit) == 0:
    print(f"Last digit of {number} is {lastdigit} and is 0")
else:
    print(f"Last digit of {number} is {lastdigit} and \
is less than 6 and not 0")
