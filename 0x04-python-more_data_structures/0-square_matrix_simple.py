#!/usr/bin/python3

"""
    ------------
    About Module
    ------------
    computes the square value of all integers of a matrix

    ---------
    More Info
    ---------
    @matrix: this is a list of lists
"""


def square_matrix_simple(matrix=[]):

    """ Create an empty list """
    dbl_matrix = []

    """ Double the contents of matrix and save them in dbl_matrix """
    for num in matrix:
        dbl_matrix.append(list(map((lambda elem: elem ** 2), num)))

    """ Return the new doubled list """
    return (dbl_matrix)
