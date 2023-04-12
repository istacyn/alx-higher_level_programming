#!/usr/bin/python3
"""This module creates an object from a JSON file"""
import json


def load_from_json_file(filename):
    """
    Creates an Object from a "JSON file".

    Args:
    filename: JSON file that object is created from.
    """
    with open(filename, 'r') as file:
        return json.load(file)
