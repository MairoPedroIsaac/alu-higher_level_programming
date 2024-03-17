#!/usr/bin/python3
"""
Script that adds all arguments to a Python list,
and then saves them to a file named add_item.json
"""

import sys
import json
from os import path

# Importing custom functions from previous scripts
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

# File name for storing the list
file_name = "add_item.json"

# Check if the file exists
if not path.exists(file_name):
    # If the file doesn't exist, create an empty list
    data = []
else:
    # If the file exists, load the data from it
    data = load_from_json_file(file_name)

# Add command line arguments to the list
data.extend(sys.argv[1:])

# Save the updated list to the file
save_to_json_file(data, file_name)

