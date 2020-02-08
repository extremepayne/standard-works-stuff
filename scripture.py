"""Defines a python interface for interacting with the scriptures."""
# pylint: disable=C0103
import json
import random
from textwrap import wrap

# Read JSON file into dicts
file_path = "lds-scriptures.json"

# Define method
def get_random_verse():
    """
    Produce a random verse.
    """
    with open(file_path, "r") as scripture_file:
        file_list = open(file_path).readlines()
        length_of_file = len(file_list)
        verse_number = random.randint(0, length_of_file)
        verse = file_list[verse_number]
    return verse
    
