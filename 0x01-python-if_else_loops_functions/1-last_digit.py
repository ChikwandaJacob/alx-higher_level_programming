#!/usr/bin/python3

import random

number = random.randint(-10000, 10000)

text = str(number)

last_digit = int(text[len(text) - 1])

if number < 0:
    last_digit *= -1

if last_digit > 5:
    text = "and is greater than 5"
elif last_digit < 6 and last_digit != 0:
    text = "and is less than 6 and not 0"
else:
    text = "and is 0"

print("Last digit of {:d} is {:d} {:s}".format(number, last_digit, text))
