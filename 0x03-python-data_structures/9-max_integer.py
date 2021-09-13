#!/usr/bin/python3

"""
    ------------
    About Module
    ------------
    Finds the biggest integer of a list.

    ---------
    More Info
    ---------
    @my_list: list to be worked on.

    if list is empty return "None"
"""


def max_integer(my_list=[]):

    """ Get the index of last element """
    last_index = len(my_list) - 1

    """ Check if list is empty """
    if last_index < 0:
        max = "None"
    else:

        """ Sort the list """
        my_list.sort()

        """ Get the max value """
        max = my_list[last_index]

    return (max)
