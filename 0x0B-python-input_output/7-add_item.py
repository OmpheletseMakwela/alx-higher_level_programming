#!/usr/bin/python3
"""import a module"""
import sys
from os import path
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

args = sys.argv[1:]  # Get all command-line arguments except the script name

filename = "add_item.json"

# If the file doesn't exist, create an empty list
if not path.exists(filename):
    save_to_json_file([], filename)

# Load the existing list from the file
items_list = load_from_json_file(filename)

# Add new arguments to the existing list
items_list.extend(args)

# Save the updated list to the file
save_to_json_file(items_list, filename)
