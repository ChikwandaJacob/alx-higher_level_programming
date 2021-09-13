#!/usr/bin/python3

"""
    ------------
    About Module
    ------------
    Finds all multiples of 2 in a list.

    ---------
    More Info
    ---------
    @my_list: list to be worked on.

    Return a list with true or false values for each element.
"""


def divisible_by_2(my_list=[]):

    """ Define an empty list """
    new_list = []

    """ Loop through the list """
    for digit in my_list:

        """ Check whether digit is a multiple of 2 """
        if digit % 2 == 0:
            new_list.append(True)
        else:
            new_list.append(False)

    """ Return new list """
    return (new_list)
