#!/usr/bin/python3

"""
    ------------
    About Module
    ------------
    returns a new dictionary with all values multiplied by 2

    ---------
    More Info
    ---------
    takes a dictionary
"""


def multiply_by_2(a_dictionary):

    """ Make a copy of the dictionary """
    dict_a = a_dictionary.copy()

    """ Get keys """
    keys = list(dict_a.keys())

    """ Update the values """
    for key in keys:

        dict_a.update({key: (dict_a[key] * 2)})

    return (dict_a)
