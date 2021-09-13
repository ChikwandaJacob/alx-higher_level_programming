#!/usr/bin/python3

"""
    ------------
    About Module
    ------------
    Replaces an element in a list without modifying the original list

    ---------
    More Info
    ---------
    @idx: index of element to be replaced.
    @my_list: list to be worked on.
    @element: element to be replaced.

    List bound checking will be done.
"""


def new_in_list(my_list, idx, element):

    """ Make a copy of the list """
    new_list = my_list.copy()

    """ Check for bounds and make modifications """
    bound = len(my_list) - 1

    if (idx < 0 or idx > bound):
        return (new_list)
    else:
        new_list[idx] = element

        return (new_list)
