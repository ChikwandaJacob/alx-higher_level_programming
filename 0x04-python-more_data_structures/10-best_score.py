#!/usr/bin/python3

"""
    ------------
    About Module
    ------------
    returns a key with the biggest integer value.

    ---------
    More Info
    ---------
    takes a dictionary
    * Assume all values of the dictionary are integers
"""


def best_score(a_dictionary):

    """ Check type of argument """
    if type(a_dictionary) != dict:
        return ("None")

    """ Get keys & populate scores list """
    scores = list(a_dictionary.values())

    """ Sort the scores """
    scores.sort()

    """ Store the maximum value """
    max_value = scores[len(scores) - 1]

    """ Search for the key with max value """
    for key, value in a_dictionary.items():

        if value == max_value:
            return (key)

    """ Return nothing. Since no max score found """
    return ("None")
