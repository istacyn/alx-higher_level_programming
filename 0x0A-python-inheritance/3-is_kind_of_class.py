#!/usr/bin/python3
"""This module checks whether an object is an instance of
or if an object is an instance of a class inherited from specified
class"""


def is_kind_of_class(obj, a_class):
    """
    Args:
        obj: object to be checked
        a_class: class to be checked against

    Returns:
        True, otherwise, False
    """
    return isinstance(obj, a_class)
