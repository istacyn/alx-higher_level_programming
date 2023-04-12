#!/usr/bin/python3
"""This module returns JSON representation of an object(string)"""
import json


def to_json_string(my_obj):
    """
    Returns JSON representation of a string object.

    Args:
    my_obj (str): Object to convert to JSON.

    Returns:
    str: JSON representation of the object
    """
    return json.dumps(my_obj)
