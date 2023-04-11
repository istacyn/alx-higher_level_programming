#!/usr/bin/python3
"""class Square that inherits from Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ This class represents the square shape"""
    def __init__(self, size):
        """
        Initialize a new instance of square class

        Arg:
        size (int): size of square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
