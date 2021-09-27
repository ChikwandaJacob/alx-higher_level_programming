#!/usr/bin/python3

"""
    ------------
    About Module
    ------------
    prints intergers only

    ---------
    More Info
    ---------
    returns false if value is not interger
"""


def safe_print_integer(value):

    try:
        print("{:d}".format(value))

        return (True)

    except Exception:
        return (False)
