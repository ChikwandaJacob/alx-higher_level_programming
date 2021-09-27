#!/usr/bin/python3

"""
    ------------
    About Module
    ------------
    prints x elements of a list.

    ---------
    More Info
    ---------
    x represents the number of elements to print
    x can be bigger than the length of my_list
"""


def safe_print_list(my_list=[], x=0):

    number_of_elements = 0

    try:
        for element in range(x):
            print("{}".format(my_list[element]), end="")
        print("")

        return (x)
    except Exception:
        for x in my_list:
            number_of_elements += 1
        print("")

        return (number_of_elements)
