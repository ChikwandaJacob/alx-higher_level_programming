#!/usr/bin/python3

""" Prevent Code Execution when script imported elsewhere """
if __name__ == "__main__":

    """ Import module that contains add, sub, mul and div functions """
    from calculator_1 import add, sub, mul, div

    """ Define two variables a and b to store some values """
    a = 10
    b = 5

    """ Print sum of a and b """
    print("{} + {} = {}".format(a, b, add(a, b)))

    """ Print difference of a and b """
    print("{} - {} = {}".format(a, b, sub(a, b)))

    """ Print product of a and b """
    print("{} * {} = {}".format(a, b, mul(a, b)))

    """ Print quotient of a and b """
    print("{} / {} = {}".format(a, b, div(a, b)))
