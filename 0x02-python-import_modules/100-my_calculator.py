#!/usr/bin/python3

"""
-------------------
Program Description
-------------------
- Imports all functions from the file calculator_1.py
and handles basic operations.
- Usage: ./100-my_calculator.py a operator b

-----------------
Program Handlings
-----------------
If operator is invalid:
print `Unknown operator. Available operators: +, -, * and /`
followed with a new line

If the number of arguments is not 3, your program has to:
print `Usage: ./100-my_calculator.py <a> <operator> <b>`
followed with a new line

All these should exit with code status 1

---------------
Expected Output
---------------
Output after operation should look like this:
<a> <operator> <b> = <result>, followed by a new line

-----------
Assumptions
-----------
All arguments will be castable into integers
"""

if __name__ == "__main__":

    """ Import sys and calculator_1 module using PEP8 standard"""
    import sys
    from calculator_1 import add, sub, div, mul

    """ Retrieve command line arguments """
    argv = sys.argv
    argc = len(argv)

    """ Handle argc != 4 problem """
    if argc != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    """ Define helper variable(s) """
    operators = ["+", "-", "*", "/"]

    a_position = 1
    operator_position = 2
    b_position = 3

    operator = argv[operator_position]
    a = int(argv[a_position])
    b = int(argv[b_position])

    """ Handle invalid operator """
    if not operator in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    """ Match the operator and print appropriate result """
    if operator == "*":
        print("{} * {} = {}".format(a, b, mul(a, b)))
    elif operator == "+":
        print("{} + {} = {}".format(a, b, add(a, b)))
    elif operator == "-":
        print("{} - {} = {}".format(a, b, sub(a, b)))
    else:
        print("{} / {} = {}".format(a, b, div(a, b)))
