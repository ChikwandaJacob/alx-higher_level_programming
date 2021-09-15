#!/usr/bin/python3

"""
    ------------
    About Module
    ------------
    replaces or adds key/value in a dictionary.

    ---------
    More Info
    ---------
    @a_dictionary: dictionary
    @key: string value of the new/existing key
    @value: value of this new element
"""


def update_dictionary(a_dictionary, key, value):

    """ Update or add new element to dictionary """

    a_dictionary.update({key: value})

    return (a_dictionary)
