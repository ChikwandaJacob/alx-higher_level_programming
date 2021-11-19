#!/usr/bin/python3

for num in range(0, 100):

    if num < 99:
        print("{:s}".format(
            "0" + str(num) if num <= 9 else str(num)), end=", ")
    else:
        print("{:d}".format(num))
