#!/usr/bin/python3

def complex_delete(a_dictionary, value):

    d = a_dictionary.copy()

    for key, d_value in d.items():

        if d_value == value:
            a_dictionary.pop(key)

    return (a_dictionary)
