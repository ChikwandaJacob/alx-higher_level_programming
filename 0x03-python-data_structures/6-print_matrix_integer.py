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

    """ Define a loop counter variable """
    counter = 0

    """ Print the list """
    for matrix_list in matrix:
        for item in matrix_list:
            if counter != len(matrix_list) - 1:
                print("{:d}".format(item), end=" ")
            else:
                print("{:d}".format(item), end="")

            counter += 1

        """ Print New Line """
        print("")

        """ Reset counter """
        counter = 0
