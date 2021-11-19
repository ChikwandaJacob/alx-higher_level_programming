#!/usr/bin/python3
def uppercase(str):
    for letter in str:

        asci_val = ord(letter)
        print("{:s}".format(
            chr(asci_val - 32)
            if asci_val >= 97 and asci_val <= 123
            else chr(asci_val)), end="")

    print("")
