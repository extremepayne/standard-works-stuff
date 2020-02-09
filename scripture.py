"""Defines a python interface for interacting with the scriptures."""
# pylint: disable=C0103
import json
import random
import textwrap

file_path = "lds-scriptures.json"


def get_random_verse():
    """Produce a random verse."""
    with open(file_path, "r") as scripture_file:
        file_list = open(file_path).readlines()
        length_of_file = len(file_list)
        verse_number = random.randint(0, length_of_file)
        verse_json = file_list[verse_number]
        verse = json.loads(verse_json)
    return verse


def pretty_print_verse(verse):
    to_return = verse["verse_title"]
    to_return += ": \n"
    wrapped_verse = textwrap.wrap(verse["scripture_text"])
    for line in wrapped_verse:
        to_return += line + "\n"
    return to_return
