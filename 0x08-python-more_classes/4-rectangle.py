#!/usr/bin/python3
"""class Rectangle that defines a rectangle"""


class Rectangle:
    """class definition"""

    def __init__(self, width=0, height=0):
        """instatiation with optional
        width and height parameters
        """
        self.width = width
        self.height = height

    """property to retrieve width attribute"""
    @property
    def width(self):
        return self.__width

    """property setter to set width attribute"""
    @width.setter
    def width(self, value):
        """isinstance() function to check if a value is integer"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    """property to retrieve height attribute"""
    @property
    def height(self):
        return self.__height

    """property setter to set height attribute"""
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    """returns the rectangle area"""
    def area(self):
        return (self.__width * self.__height)

    """returns the rectangle perimeter:"""
    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ("")
        rectangle_str = ""
        for x in range(self.__height):
            rectangle_str += "#" * self.__width
            if x < self.__height - 1:
                rectangle_str += "\n"
        return rectangle_str

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)
