#!/usr/bin/python3

"""
    ------------
    About Module
    ------------
    Deletes item at a specific position in a list.

    ---------
    More Info
    ---------
    @my_list: list to be worked with.
    @idx: index of the item to be removed.

    if idx < 0 or out of range do nothing.
    pop() function should not be used.
"""


def delete_at(my_list=[], idx=0):

    """ Perform checks on idx """
    bound = len(my_list) - 1

    if (idx < 0 or idx > bound):
        return (my_list)
    else:

        """ Make a copy of the original list """
        list_copy = my_list.copy()

        """ Clear the original list """
        my_list.clear()

        """ Loop through the copied list """
        for index in range(bound + 1):

            """ Perform checks """
            if index != idx:
                my_list.append(list_copy[index])
            else:
                continue

    """ Return the new list """
    return (my_list)
