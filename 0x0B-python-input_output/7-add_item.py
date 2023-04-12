#!/usr/bin/python3
"""This module adds all arguments to a Python list and saves them to a file"""


import sys
from 5-save_to_json_file.py import save_to_json_file
from 6-load_from_json_file.py import load_from_json_file


# Load current list from file or create empty list
try:
    list = load_from_json_file("add_item.json")
except FileNotFoundError:
    list = []

# Add command-line arguments to the list
for arg in sys.argv[1:]:
    list.append(arg)

# Save updated list to file
save_to_json_file(list, "add_item.json")
