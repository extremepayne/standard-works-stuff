"""select a random verse"""
# pylint: disable=C0103
import json
import random

file_path = "lds-scriptures.json"

scriptures = []

with open(file_path, "r") as scripture_file:
    length_of_file = len(open(file_path).readlines())
    i = 0
    while i < length_of_file - 1:
        verse = scripture_file.readline()
        verse = json.loads(verse)
        scriptures.append(verse)
        i += 1


def get_random_verse(volume_id="all"):
    if volume_id == "all":
        return random.choice(scriptures)
    elif isinstance(volume_id, int) and volume_id >=1 and volume_id <= 5:
        return("unimplemented.")
    else:
        raise TypeError


rand_verse = get_random_verse()
print(rand_verse["verse_title"], rand_verse["scripture_text"], sep=': ')
print(rand_verse)
