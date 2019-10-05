"""
Defines a python interface for interacting with the scriptures.

Includes: lists of dicts representing verses:
    scriptures: all standard works
    book_of_mormon: only verses from the BoM
    doctrine_and_covenants: only verses from the D&C
    new_testament: only verses from the NT
    old_testament: only verses from the OT

Functions for doing things:
    get_random_verse: returns a psuedo-random verse
    generate_scripture_url: Generate the url to a verse or chapter
"""
# pylint: disable=C0103
import json
import random
from textwrap import wrap

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


def generate_scripture_url(location, chapter=False):
    """Generate a url to the actual scripture."""
    to_return = "https://www.churchofjesuschrist.org/study/scriptures/"
    if isinstance(location, dict) and "volume_lds_url" in location:
        verse = location
        # We assume that the location provided is a verse dcitionary
        if verse["volume_lds_url"] == "bm":
            to_return += "bofm"
        elif verse["volume_lds_url"] == "dc":
            to_return += "dc-testament"
        else:
            to_return += verse["volume_lds_url"]
        if not chapter:
            to_return = (
                to_return
                + "/"
                + verse["book_lds_url"]
                + "/"
                + str(verse["chapter_number"])
                + "."
                + str(verse["verse_number"])
                + "?lang=eng#"
            )
            if verse["verse_number"] == 1:
                return to_return + "p1"
            else:
                return to_return + str(verse["verse_number"] - 1)
        else:  # Give a url to the chapter that the verse is in
            to_return = (
                to_return
                + "/"
                + verse["book_lds_url"]
                + "/"
                + str(verse["chapter_number"])
            )
            return to_return
    else:  # Hope they gave us a volume string
        return to_return + location


class Verse:
    """A verse of scripture."""

    def __init__(self, verse_dict):
        """Initialize a verse."""
        self.verse_dictionary = verse_dict
        self.id = verse_dict["verse_id"]
        self.text = verse_dict["scripture_text"]
        self.title = verse_dict["verse_title"]
        self.url = generate_scripture_url(verse_dict)
        self.chapter = None

    def __str__(self):
        """Print out the verse's title, text, and url."""
        out = ""
        wrapped_verse = wrap(self.text)
        out += self.title + ": \n"
        for line in wrapped_verse:
            out += line + "\n"
        return out + self.url


class Chapter:
    """A chapter of scripture."""

    def __init__(self, id, verses):
        """Initialize a chapter."""
        self.id = id
        self.verses = verses
        for verse in verses:
            verse.chapter = self

    def __str__(self):
        """Return chapter id."""
        return str(self.id)


scriptures_objects = []
chapter_objects = []
verses_in_chapters = {}
biggest_chapter_id = 0

for verse_dictionary in scriptures:
    new_verse = Verse(verse_dictionary)
    scriptures_objects.append(new_verse)
    if verse_dictionary["chapter_id"] > biggest_chapter_id:
        verses_in_chapters[verse_dictionary["chapter_id"]] = []
        biggest_chapter_id = verse_dictionary["chapter_id"]
    verses_in_chapters[verse_dictionary["chapter_id"]].append(new_verse)

for i in range(1, biggest_chapter_id + 1):
    new_chapter = Chapter(i, verses_in_chapters[i])
    chapter_objects.append(new_chapter)
print(scriptures_objects[1900].chapter)


def get_random_verse(volume_id="all"):
    """
    Produce a random verse.

    Can be from all standard works (default) or a specific one.
    """
    if volume_id == "all":
        return random.choice(scriptures_objects)
    elif isinstance(volume_id, int) and volume_id >= 1 and volume_id <= 5:
        return random.choice(books_of_scripture[volume_id])
    else:
        raise TypeError
