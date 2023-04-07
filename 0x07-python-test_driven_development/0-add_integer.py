#!/usr/bin/python3
"""
Function that adds two integers
"""


def add_integer(a, b=98):
    """
    Function that adds two integer numbers
    that must be an integers or floats

    Args:
        a: The first number to add.
        b: The second number to add.

    raises:
        TypeError if a or b is not an integer or a float

    return:
        The sum of a and b
    """

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)

    return a + b
