#!/usr/bin/python3
"""This module creates a square"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Represents a square. Inherits from the Rectangle Class.
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a new instance of the Square class.
        Args:
        size: The size of the square.
        x: The x-coordinate of the square.
        y: The y-coordibate of the square.
        id: The id of the square.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Create a string representation of Square class"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    @property
    def size(self):
        """Gets the size of the square"""
        return self.width

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.
        Args:
        value(int): The new size value.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updates attributes of Square class
        with given arguments"""
        if args:
            for index, value in enumerate(args):
                if index == 0:
                    self.id = value
                elif index == 1:
                    self.size = value
                elif index == 2:
                    self.x = value
                elif index == 3:
                    self.y = value
        else:
            for k, v in kwargs.items():
                if k == 'id':
                    self.id = v
                elif k == 'size':
                    self.size = v
                elif k == 'x':
                    self.x = v
                elif k == 'y':
                    self.y = v

    def to_dictionary(self):
        """Returns the dictionary representation of a Square"""
        return {'id': self.id, 'size': self.width,
                'x': self.x, 'y': self.y}
