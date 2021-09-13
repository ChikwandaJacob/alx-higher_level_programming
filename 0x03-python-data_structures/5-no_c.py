#!/usr/bin/python3

"""
    ------------
    About Module
    ------------
    Removes all characters c and C from a string.

    ---------
    More Info
    ---------
    @my_string: string to be stripped of aforementioned characters.
"""


def no_c(my_string):

    """ Convert string to list """
    str_list = list(my_string)

    """ Replace all c characters """
    while 'c' in str_list:
        str_list.pop(str_list.index('c'))

    """ Replace all C charcaters """
    while 'C' in str_list:
        str_list.pop(str_list.index('C'))

    """ Convert list to string """
    final_string = ''.join(map(str, str_list))

    return (final_string)
