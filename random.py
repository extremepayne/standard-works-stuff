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

length = len(scriptures)
choice = random.randint(length)
print(scriptures[choice])
