#!/usr/bin/python3
"""This module defines a student"""


class Student():
    """This class defines a student"""
    def __init__(self, first_name, last_name, age):
        """
        Initialize first name, last name and age of a student.
        Args:
        first_name: The student's first name.
        last_name: The students last name.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        Args:
        attrs: List of attribute names to retrieve
        """
        if attrs if None:
            return self.__dict__
        else:
            return {attr: getattr(self, attr) for attr in attrs
                    if hasattr(self, attr)}
