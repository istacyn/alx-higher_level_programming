#!/usr/bin/python3
"""This modele comp[ares if the object is exactly
an instance of the specified class"""


def is_same_class(obj, a_class):
    """
    Args:
        obj: object to be checked
        a_class: class to be compared to obj

    Return:
        True, otherwise, Falsw
    """
    return type(obj) is a_class
