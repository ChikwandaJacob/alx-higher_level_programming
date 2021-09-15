#!/usr/bin/python3

"""
    ------------
    About Module
    ------------
    converts a Roman numeral to an integer.

    ---------
    More Info
    ---------
    takes a string in roman numeral form
"""


def roman_to_int(roman_string):

    """ Check if string is valid """
    if type(roman_string) != str:
        return (0)

    """ Split the string into parts """
    rom_str = list(roman_string)

    """ Define a dictionary of roman values """
    rom_num = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    """ Get keys """
    symbols = list(rom_num.keys())

    """ Loop through """
    result = 0

    for sym in rom_str:

        if sym in symbols:
            result += rom_num[sym]

    """ Return the result """
    return (result)
