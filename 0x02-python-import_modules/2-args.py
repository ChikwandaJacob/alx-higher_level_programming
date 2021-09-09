#!/usr/bin/python3

"""
-------------------
Program Description
-------------------
prints the number of and the list of its arguments.
"""

""" Ensure code won't be executed when imported elsewhere """
if __name__ == "__main__":

    """ Import sys module so as to access command line arguments """
    import sys

    """ Retrieve all command line arguments and the length of the list """
    argv = sys.argv
    argc = len(argv) - 1

    """ Print outcome based on given predicate """
    if argc == 0:
        print("{} arguments.".format(argc))
    elif argc == 1:
        print("{} argument:".format(argc))
        print("{}: {}".format(argc, argv[1]))
    else:
        print("{} arguments:".format(argc))
        for index in range(1, argc + 1):
            print("{}: {}".format(index, argv[index]))
