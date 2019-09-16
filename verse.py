"""select a random verse"""
# pylint: disable=C0103
import json
import random

file_path = "lds-scriptures.json"

scriptures = []
book_of_mormon = []
doctrine_and_covenants = []
new_testament = []
old_testament = []
pearl_of_great_price = []
books_of_scripture = {
    1: old_testament,
    2: new_testament,
    3: book_of_mormon,
    4: doctrine_and_covenants,
    5: pearl_of_great_price,
}

with open(file_path, "r") as scripture_file:
    length_of_file = len(open(file_path).readlines())
    i = 0
    while i < length_of_file - 1:
        verse = scripture_file.readline()
        verse = json.loads(verse)
        scriptures.append(verse)
        books_of_scripture[verse["volume_id"]].append(verse)
        i += 1


def get_random_verse(volume_id="all"):
    """
    Using the defined dictionaries, get a random verse.

    Can be from all standard works (default) or a specific one.
    """
    if volume_id == "all":
        return random.choice(scriptures)
    elif isinstance(volume_id, int) and volume_id >= 1 and volume_id <= 5:
        return random.choice(books_of_scripture[volume_id])
    else:
        raise TypeError

def generate_churchofjesuschrist_url(verse):
    to_return = "https://www.churchofjesuschrist.org/study/scriptures/"
    if verse["volume_lds_url"] != "bm":
        to_return += verse["volume_lds_url"]
    else:
        to_return += "bofm"
    return to_return + "/" + verse["book_lds_url"] + "/" + str(verse["chapter_number"]) \
    + "." + str(verse["verse_number"]) + "?lang=eng#" + str(verse["verse_number"] - 1)

rand_verse = get_random_verse()
print("Random verse: ")
print(rand_verse["verse_title"], rand_verse["scripture_text"], sep=': ')
print(generate_churchofjesuschrist_url(rand_verse))

# rand_verse = get_random_verse(3)  # from the book of mormon
# print("\nRandom verse, but only from the book of mormon: ")
# print(rand_verse["verse_title"], rand_verse["scripture_text"], sep=': ')
