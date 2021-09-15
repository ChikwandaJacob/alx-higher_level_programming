#!/usr/bin/python3


def weight_average(my_list=[]):

    if (len(my_list) == 0):
        return (0)

    """ Get total weights """
    weight_by_score = 0
    cum_weight = 0

    for item in my_list:

        weight_by_score += (item[0] * item[1])
        cum_weight += item[1]

    return (weight_by_score / cum_weight)
