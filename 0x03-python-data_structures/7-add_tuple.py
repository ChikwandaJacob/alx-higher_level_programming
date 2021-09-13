#!/usr/bin/python3

"""
    ------------
    About Module
    ------------
    Adds 2 tuples.

    ---------
    More Info
    ---------
    @tuple_a: first tuple.
    @tuple_b: second tuple.

    This module will return a tuple with two intergers.

    If a tuple < 2, use the value 0 for each missing integer
    If a tuple > 2, use only the first 2 integers
"""


def add_tuple(tuple_a=(), tuple_b=()):

    """ Get tuple values """
    tup1_list = get_tuple_values(tuple_a)
    tup2_list = get_tuple_values(tuple_b)

    """ Add tuple values """
    elem1 = tup1_list[0] + tup2_list[0]
    elem2 = tup1_list[1] + tup2_list[1]

    """ Define new tuple and return it """
    new_tup = (elem1, elem2)

    return (new_tup)


def get_tuple_values(tup):

    """ Check tuple lengths """
    if len(tup) < 2:
        if (len(tup) <= 0):
            values = [0, 0]
        else:
            values = [tup[0], 0]
    elif len(tup) >= 2:
        values = [tup[0], tup[1]]

    return (values)
