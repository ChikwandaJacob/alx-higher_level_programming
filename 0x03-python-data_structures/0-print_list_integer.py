#!/usr/bin/python3

"""
-------------------
Program Description
-------------------

This file contains a function that prints all integers of a list. 
"""

if __name__ == "__main__":
    def print_list_integer(my_list=[]):

        """ Loop through the provided list """
        for item in my_list:
            print("{}".format(item))
