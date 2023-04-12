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

    def to_json(self):
        """
        Retrieves a dictionary representation of a Student instance.
        """
        return self.__dict__
