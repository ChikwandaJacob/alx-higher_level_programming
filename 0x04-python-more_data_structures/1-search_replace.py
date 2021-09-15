#!/usr/bin/python3

"""
    ------------
    About Module
    ------------
    replaces all occurrences of an element by another in a new list.

    ---------
    More Info
    ---------
    @my_list: the list to be worked with.
    @search: the element to replace in the list.
    @replace: the new element.
"""


def search_replace(my_list, search, replace):

    """ Make a copy of the list """
    my_list_cp = my_list.copy()

    """ Loop through list and do replace search value """

    for num in my_list_cp:

        if num == search:
            my_list_cp[my_list_cp.index(search)] = replace

    """ Return the list """
    return (my_list_cp)
