#!/usr/bin/python3

"""
   This class defines a sqaure
"""


class Square:

    """
       This class contains no class attributes.
       This class has one public class method called area
    """

    def __init__(self, size=0):

        """
           The init method contains one private instance attribute size

           __init__ raises two exceptions:
           1. TypeError when size is not an integer
           2. ValueError when size is less than 0
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        elif size < 0:
            raise ValueError("size must be >= 0")

        else:
            self.__size = size

    def area(self):

        """
           This method simply returns the area of the square
        """
        return (self.__size ** 2)
