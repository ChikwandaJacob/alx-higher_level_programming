#!/usr/bin/python3

import random

number = random.randint(-10, 10)

# If number is greater than or equal to 0 print its positive
# Otherwise if number is less than 0 print its negative
if number >= 0:
    print("{} is positive".format(number))
else:
    print("{} is negative".format(number))
