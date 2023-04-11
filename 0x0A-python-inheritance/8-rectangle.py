#!/usr/bin/python3
"""class Rectangle that inherits from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """This class represents the rectangle shape"""

    def __init__(self, width, height):
        """
        Initializes a new instance of Rectangle class

        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
