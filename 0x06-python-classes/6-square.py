#!/usr/bin/python3

"""
   This class defines a sqaure
"""


class Square:

    """
       This class contains no class attributes.
       This class has 3 public class methods:

       1. area(self) - returns area of the square
       2. size(self) - retrieves square size instance attribute
       3. size(self, value) - sets the square size
       4. my_print(self) - prints sqaure
       5. position(self) - retrieves position value
       6. position(self, value) - sets sqaure position values
    """

    def __init__(self, size=0, position=(0, 0)):

        """
           The init method contains one private instance attribute size

           Args:
           @size: this is the size of the square
           @position: these are the sqaure coordinates

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

        if ((isinstance(position[0], int) and isinstance(position[1], int)
             and position[0] >= 0 and position[1] >= 0)):
            self.__position = position
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):

        """
           This method simply returns the area of the square
        """
        return (self.__size ** 2)

    @property
    def size(self):

        """ Retrieves the size of the sqaure """
        return (self.__size)

    @size.setter
    def size(self, value):

        """
           Sets the value of the sqaure size

           Args:
           @value: new value for square
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        elif value < 0:
            raise ValueError("size must be >= 0")

        else:
            self.__size = value

    def my_print(self):

        """
           Prints square using #

           if size is equal to 0, print an empty line
        """
        if self.__size <= 0:
            print("")

        else:
            for i in range(self.size):
                print(" " * self.__position[0] + "#" * self.size)

    @property
    def position(self):

        """ Returns the position of the square """
        return (self.__position)

    @position.setter
    def position(self, value):

        """ Sets the new position values """
        if ((isinstance(value[0], int) and isinstance(value[1], int)
             and value[0] >= 0 and value[1] >= 0)):
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")
