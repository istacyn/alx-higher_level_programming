#!/usr/bin/python3
"""This module creates a file appending function"""


def append_write(filename="", text=""):
    """
    Appends a string to the end of a text file (UTFS)

    Args:
    filename (str): The name of the file to append the string to.
    text (str): The string to append to the file

    Returns:
    int: The number of charcters added.
    """
    with open(filename, mode='a', encoding="utf-8") as file:
        num_chars = file.write(text)
    return num_chars
