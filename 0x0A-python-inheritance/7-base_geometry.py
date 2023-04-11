#!/usr/bin/python3
"""Defines base geometry class"""


class BaseGeometry:
    """class representing a base geometry"""

    def area(self):
        """Yet to be implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates value

        Args:
            name: The name of value being validate
            value: The va;ue being validated

        Raises:
            TypeError: If value is not an integer
            ValueError: If value is less or equal to 0
        """
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
