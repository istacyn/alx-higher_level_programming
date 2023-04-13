#!/usr/bin/python3
"""This module inserts a line of text to a file,
after each line containing a specific string """


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text to a file,
    after each line containing a specific string

    Args:
    filename (str): The name of the file to modify.
    search_string (str): The string to search for.
    new_string (str): The string to insert.
    """
    with open(filename) as file:
        for line in file:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, 'w') as file:
        file.write(text)
