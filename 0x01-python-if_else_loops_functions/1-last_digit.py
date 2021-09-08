#!/usr/bin/python3

import random

number = random.randint(-10000, 10000)

# Convert random generated number into string
text = str(number)

# Store last digit
last_digit = int(text[len(text) - 1])

# Ensure last digit has same sign as origial number
if number < 0:
    last_digit *= -1

# Do some checks on the last digit
if last_digit > 5:
    text = "and is greater than 5"
elif last_digit < 6 and last_digit != 0:
    text = "and is less than 6 and not 0"
elif last_digit == 0:
    text = "and is 0"

# Print last digit
print("Last digit of {:d} is {:d} {:s}".format(number, last_digit, text))