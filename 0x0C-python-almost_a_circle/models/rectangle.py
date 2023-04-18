#!/usr/bin/python3
"""This module creates a rectangle"""


from models.base import Base


class Rectangle(Base):
    """
    Represents a rectangle. Inherits from the Base Class.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a new instance of the Rectangle class.

        Args:
        width: The width of the rectangle.
        height: The height of the rectangle.
        x: The x-coordinate of the rectangle.
        y: The y-coordibate of the rectangle.
        id: The id of the rectangle.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Gets the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle.

        Args:
        value(int): The new width value.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Gets the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle.

        Args:
        value(int): The new height value.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Gets the x-coordinate of the rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        """
        Sets the x-coordinate of the rectangle.

        Args:
        value(int): The new x-coordinate value.
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Gets the y-coordinate of the rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        """
        Sets the y-coordinate of the rectangle.

        Args:
        value(int): The new y-coordinate value.
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns the area value of the Rectangle instance"""
        return self.width * self.height

    def display(self):
        """Prints the Rectangle instance with '#' characters"""
        for i in range(self.y):
            print("")
        for i in range(self.height):
            for j in range(self.x):
                print(" ", end="")
            print("#" * self.width)

    def __str__(self):
        """Create a string representation of Rectangle class"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)

    def update(self, *args, **kwargs):
        """Updates attributes of Rectangle class
        with given arguments"""
        # Assign values from variable arguments
        for a, arg in enumerate(args):
            if a == 0 and a is not None:
                self.id = arg
            elif a == 1:
                self.width = arg
            elif a == 2:
                self.height = arg
            elif a == 3:
                self.x = arg
            elif a == 4:
                self.y = arg
        # Assign values from keyword arguments
        for key, value in kwargs.items():
            if key == 'id':
                self.id = value
            elif key == 'width':
                self.width = value
            elif key == 'height':
                self.height = value
            elif key == 'x':
                self.x = value
            elif key == 'y':
                self.y = value

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle"""
        return {'id': self.id, 'width': self.width,
                'height': self.height, 'x': self.x, 'y': self.y}
