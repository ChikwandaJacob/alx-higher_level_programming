#!/usr/bin/python3

"""
    ------------
    About Module
    ------------
    Returns a tuple with the length of a string and its first character.

    ---------
    More Info
    ---------
    @sentence: string to work with.

    if string is empty the first character should be None.
"""


def multiple_returns(sentence):

    """ Get length of the string """
    string_len = len(sentence)

    """ Check the length of the string """
    if string_len == 0:
        tup = (string_len, "None")
    else:
        tup = (string_len, sentence[0])

    return (tup)
