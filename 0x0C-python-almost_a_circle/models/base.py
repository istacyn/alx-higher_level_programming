#!/usr/bin/python3
"""This module creates a base class for
all other classes in this project"""


class Base:
    """
    Base class for creating objects with unique ids.

    Attributes:
    __nb_objects: Keeps track of number of instances created and
    assigns unique id to them.

    id: Holds unique id for ech instance of the class.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        The constructor for the Base class.

        Args:
        id (int): The id assigned to the instance.
        If not provided, unique id will be generated using
        __nb_objects attribute.
        """
        if id is not None:
            self.id = id
        else:
            self.__class__.__nb_objects += 1
            self.id = self.__class__.__nb_objects
