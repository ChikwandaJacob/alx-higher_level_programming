#!/usr/bin/python3

"""
    ------------
    About Module
    ------------
    prints intergers

    ---------
    More Info
    ---------
    returns number of intergers in a list
"""


def safe_print_list_integers(my_list=[], x=0):

    number_of_elements = 0

    try:
        for element in range(x):

            if (isinstance(my_list[element], int)):
                number_of_elements += 1
                print("{:d}".format(my_list[element]), end="")

        print("")
        return (number_of_elements)

    except Exception:
        print("{:d}".format(my_list[x]), end="")
