#!/usr/bin/python3

"""
    ------------
    About Module
    ------------
    Module prints all integers of a list, in reverse order.

    ---------
    More Info
    ---------
    @my_list: this is the list to be printed in reverse.
"""


def print_reversed_list_integer(my_list=[]):

    """ Reverse the string with inbuilt function """
    my_list.reverse()

    """ Print the reversed list """
    for item in my_list:
        print("{:d}".format(item))
