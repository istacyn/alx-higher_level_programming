#!/usr/bin/python3
"""This module returns an object represented by a JSON string"""
import json


def from_json_string(my_str):
    """
    Returns Python object represented by JSON string

    Args:
    my_str (str): JSON string to be converted to Python object

    Returns:
    Python object
    """
    return json.loads(my_str)
