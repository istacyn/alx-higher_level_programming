#!/usr/bin/python3
"""This module inherits list"""


class MyList(list):
    """This class inherits out of list"""
    def print_sorted(self):
        """prints the list, but sorted (ascending sort)"""
        self.sort()
        print(self)
