#!/usr/bin/python3

"""
    ------------
    About Module
    ------------
    deletes a key in a dictionary.

    ---------
    More Info
    ---------
    function takes a dictionary as well as a key
    * module handles key error
"""


def simple_delete(a_dictionary, key=""):

    """ Get all keys """
    keys = list(a_dictionary.keys())

    """ Perform check on the given key """
    if key in keys:
        a_dictionary.pop(key)

    """ Return the dictionary """
    return (a_dictionary)
