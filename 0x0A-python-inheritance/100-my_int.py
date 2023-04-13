#!/usr/bin/python3
"""MyInt that inherits from int but == and != operators inverted"""


class MyInt(int):
    """Rebel class that inverts == and != operators"""
    def __eq__(self, other):
        """
        Overrides the == operator.

        Args:
        other: Another instance of MyInt
        """
        return self.real != other

    def __ne__(self, other):
        """
        Overrides the != operator.

        Args:
        other: Another instance of MyInt
        """
        return self.real == other
