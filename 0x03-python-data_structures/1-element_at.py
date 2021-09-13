#!/usr/bin/python3

"""

    This module contains a function to retrieve an element from a list.

    if idx < 0 function returns None
    if idx out of list range function returns None

"""


def element_at(my_list, idx):

    """ Set list bound """
    bound = len(my_list) - 1

    """ Check if idx is within the bound """
    if idx < 0 or idx > bound:
        result = "None"
    else:
        result = my_list[idx]

    return (result)
