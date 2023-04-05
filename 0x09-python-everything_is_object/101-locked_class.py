#!/usr/bin/python3
"""
A locked  class that prevents the user from dynamically
creating new instance attributes.
"""


class LockedClass:
    """
    Exception if the new instance attribute is called first_name
    """

    __slots__ = ["first_name"]
