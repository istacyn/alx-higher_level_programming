#!/usr/bin/python3
"""Checks if the object is an instance of a class that inherited
from the specified class"""


def inherits_from(obj, a_class):
    """
    Args:
        obj: object to check
        a_class: class to be checked against

    Returns:
        True, otherwise, False
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
