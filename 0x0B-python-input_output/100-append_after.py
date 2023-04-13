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
        lines = file.readlines()

    with open(filename, 'w') as file:
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string + "\n")
