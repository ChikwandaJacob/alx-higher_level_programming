#!/usr/bin/python3

"""
    ------------
    About Module
    ------------
    This module replaces an element of a list at a specific position.

    ---------
    More Info
    ---------
    @idx: is the index of the element to be replaced.
    @my_list: is the list to be manipulated.
    @element: is the new element to replace the old element.

    if idx < 0 do nothing except return original list.
    if idx is out of range do nothing except return original list.
"""


def replace_in_list(my_list, idx, element):

    """ Define list bounds variable """
    bound = len(my_list) - 1

    """ Check whether idx is within the bound """
    if idx < 0 or idx > bound:
        new_list = my_list
    else:
        my_list[idx] = element
        new_list = my_list

    return (new_list)
