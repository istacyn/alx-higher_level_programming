#!/usr/bin/python3
"""class Rectangle that defines a rectangle"""


class Rectangle:
    """class definition"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializing the Rectangle class
        Args:
            width: represents the width of the rectangle
            height: represents the height of the rectangle
        Raises:
            TypeError: if size is not integer
            ValueError: if size is less than zero
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1
        """Incremented during each new instance instantiation"""

    @property
    def width(self):
        """property to retrieve width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """property setter to set width attribute"""
        if not isinstance(value, int):
            """isinstance() function to check if a value is integer"""
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """property to retrieve height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """property setter to set height attribute"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the rectangle area"""
        return (self.__width * self.__height)

    def perimeter(self):
        """returns the rectangle perimeter:"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        rectangle_str = ""
        if self.__width == 0 or self.__height == 0:
            return rectangle_str

        for x in range(self.__height):
            rectangle_str += (str(self.print_symbol) * self.__width)
            if x != self.__height - 1:
                rectangle_str += "\n"
        return rectangle_str

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """when an instance of Rectangle is deleted"""
        print("Bye rectangle...")
        """Decremented during each instance deletion"""
        Rectangle.number_of_instances -= 1
