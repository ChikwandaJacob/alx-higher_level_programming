#!/usr/bin/python3

"""
-------------------
Program Description
-------------------
prints all the names defined by the compiled module hidden_4.pyc
"""

if __name__ == "__main__":

    """ Import the module in the program description """
    import hidden_4

    """ Save contents of module in list and sort them """
    module_content = dir(hidden_4)
    module_content.sort()

    """ Define some helper variables """
    module_length = len(module_content)
    start_symbol = "__"

    """ Print Content of the list with exception of names that start with`__`"""
    for index in range(0, module_length):
        text = module_content[index]

        if start_symbol == text[:2]:
            continue
        else:
            print(text)
