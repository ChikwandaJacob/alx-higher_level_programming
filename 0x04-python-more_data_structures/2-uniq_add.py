#!/usr/bin/python3

"""
    ------------
    About Module
    ------------
    adds all unique integers in a list (only once for each integer).

    ---------
    More Info
    ---------
    @my_list: list to be worked on
"""


def uniq_add(my_list=[]):

    """ Convert the list into a set """
    integers = set(my_list)

    """ Loop through list and add numbers """
    sum = 0

    for num in integers:

        sum += num

    """ Return the sum """
    return (sum)
