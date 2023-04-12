#!/usr/bin/python3
"""This module writes object to text file using JSON representation"""
import json


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file using a JSON representation

    Args:
    my_obj: The object to write to the file
    filename: Name of file to write object to
    """
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
