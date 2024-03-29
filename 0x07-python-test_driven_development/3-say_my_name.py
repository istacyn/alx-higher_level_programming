#!/usr/bin/python3
"""
Function that prints My name is <first name> <last name>
"""


def say_my_name(first_name, last_name=""):
    """
    Prints first and last name

    Args:
    first_name: first name
    last_name: last name

    Raises:
    TypeError if first or last name is not a string
    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
