#!/usr/bin/python3

"""
-------------------
Program Description
-------------------
prints the result of the addition of all arguments passed via the command line
"""

if __name__ == "__main__":

    """ Import sys module """
    import sys

    """ Retrieve command line arguments """
    argv = sys.argv
    argc = len(argv)

    """ Define a helper variable for sum """
    total = 0

    """ Print outcome based on certain predicate """
    if argc == 1:
        print("{}".format(total))
    else:
        for i in range(1, argc):
            total += int(argv[i])

        print("{}".format(total))
