#!/usr/bin/python3

# Set Start and Stop Values
start = 0
stop = 99

# Print hex values with the help of for loop
for index in range(start, stop):
    print("{:d} = {:s}".format(index, hex(index)))