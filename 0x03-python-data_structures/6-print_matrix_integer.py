#!/usr/bin/python3

"""
    ------------
    About Module
    ------------
    prints a matrix of integers.

    ---------
    More Info
    ---------
    @matrix: list of lists to be printed
"""


def print_matrix_integer(matrix=[[]]):

    """ Print the list """
    for matrix_list in matrix:
        for item in matrix_list:
            print("{:d}".format(item), end=" ")
        print("")
