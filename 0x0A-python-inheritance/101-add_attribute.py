#!/usr/bin/python3
"""This module adds a new attribute to an object if it’s possible"""


def add_attribute(obj, attr_name, attr_value):
    """
    Adds new attribute to an object if possible.

    Args:
    obj: The object to add the new attribute to.
    attr_name (str): The name of the new attribute.
    attr_value: The value of the new attribute.

    Raises:
    TypeError: If the object cannot have a new attribute added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attr_name, attr_value)
