#!/usr/bin/python3

import sys


def safe_function(fct, *args):

    result = 0

    try:
        result = fct(args[0], args[1])

        return (result)

    except Exception as e:
        result = "Exception: " + str(e) + "\n"

        sys.stderr.write(result)

        return ("None")
