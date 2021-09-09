#!/usr/bin/python3

"""
-------------------
Program Description
-------------------
program that imports the variable a from the file variable_load_5.py
and prints its value.
"""

if __name__ == "__main__":

    """ Import aformentioned module """
    import variable_load_5 as var

    """ Print the variable of a in the module """
    print("{}".format(var.a))
