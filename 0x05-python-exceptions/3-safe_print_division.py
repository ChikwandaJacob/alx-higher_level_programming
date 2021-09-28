#!/usr/bin/python3


def safe_print_division(a, b):

    quotient = 0
    message = ""

    try:
        quotient = a / b
        message = quotient

    except ZeroDivisionError:
        quotient = "None"
        message = quotient

    finally:
        print("Inside result: {}".format(message))
        return (quotient)
