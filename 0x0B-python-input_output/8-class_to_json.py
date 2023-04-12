#!/usr/bin/python3
"""This module returns dictionary description with
simple data structure for JSON serialization of an object"""


def class_to_json(obj):
    """
    Returns the dictionary description with simple
    data structure for JSON serialization of an object

    Args:
    obj: An instance of a class.

    Returns:
    Dictionary description with simple data structure
    (list, dictionary, string, integer and boolean)
    """
    return obj.__dict__
