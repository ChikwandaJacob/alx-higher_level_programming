#!/usr/bin/python3

# Set up ASCII values for lower case letters
start = 97
stop = 123

# Loop through the values
for letter in range(start, stop):
    print("{:c}".format(letter), end='')
