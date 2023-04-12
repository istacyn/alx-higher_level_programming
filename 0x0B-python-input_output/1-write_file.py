#!/usr/bin/python3
"""This module creates a function that writes a string to a
text file and returns the number of characters written"""


def write_file(filename="", text=""):
    """Function to write a string to a text file"""
    with open(filename, mode='w', encoding="utf-8") as file:
        num_chars = file.write(text)
    return num_chars
