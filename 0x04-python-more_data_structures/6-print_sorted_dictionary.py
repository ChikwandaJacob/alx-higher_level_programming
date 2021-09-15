#!/usr/bin/python3

"""
    ------------
    About Module
    ------------
    prints a dictionary by ordered keys.

    ---------
    More Info
    ---------
    takes a dictionary as argument
"""


def print_sorted_dictionary(a_dictionary):

    """ Store all keys in a list """
    keys = list(a_dictionary.keys())

    """ Sort the list """
    keys.sort()

    """ Print the keys in the sorted order """
    for key in keys:
        print("{}: {}".format(key, a_dictionary[key]))
