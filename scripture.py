"""Defines a python interface for interacting with the scriptures."""
# pylint: disable=C0103
import json
import random
from textwrap import wrap

# Read JSON file into dicts
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


# Define classes
class Book:
    """A book of scripture."""

    def __init__(self, bk_id, verses):
        """Initialize a book."""
        self.bk_id = bk_id
        self.verses = verses
        self.chapters = []
        for verse in verses:
            verse.book = self
            if verse.chapter not in self.chapters:
                self.chapters.append(verse.chapter)
                verse.chapter.book = self
        self.book_lds_url = verses[0].book_lds_url
        self.volume_lds_url = verses[0].volume_lds_url

    def __str__(self):
        """Return book id."""
        return str(self.bk_id)

    def gen_url(self):
        """Generate this verse's churchofjesuschrist.org url."""
        to_return = "https://www.churchofjesuschrist.org/study/scriptures/"
        if self.volume_lds_url == "bm":
            to_return += "bofm"
        elif self.volume_lds_url == "dc":
            to_return += "dc-testament"
        else:
            to_return += self.volume_lds_url
        to_return = to_return + "/" + self.book_lds_url
        return to_return


class Chapter(Book):
    """A chapter of scripture."""

    def __init__(self, ch_id, verses):
        """Initialize a chapter."""
        self.ch_id = ch_id
        self.verses = verses
        for verse in verses:
            verse.chapter = self
        self.book_lds_url = verses[0].book_lds_url
        self.volume_lds_url = verses[0].volume_lds_url
        self.ch_num = verses[0].ch_num
        self.book = None

    def __str__(self):
        """Return chapter id."""
        return str(self.ch_id)

    def gen_url(self):
        """Generate this chapters' churchofjesuschrist.org url."""
        to_return = super().gen_url()
        return to_return + "/" + str(self.ch_num)


class Verse(Chapter):
    """A verse of scripture."""

    def __init__(self, verse_dict):
        """Initialize a verse."""
        self.verse_dictionary = verse_dict
        self.id = verse_dict["verse_id"]
        self.text = verse_dict["scripture_text"]
        self.title = verse_dict["verse_title"]
        self.book_lds_url = verse_dict["book_lds_url"]
        self.volume_lds_url = verse_dict["volume_lds_url"]
        self.ch_num = verse_dict["chapter_number"]
        self.chapter = None
        self.book = None
        self.url = self.gen_url()

    def __str__(self):
        """Print out the verse's title, text, and url."""
        out = ""
        wrapped_verse = wrap(self.text)
        out += self.title + ": \n"
        for line in wrapped_verse:
            out += line + "\n"
        return out + self.url

    def gen_url(self):
        """Generate this verse's churchofjesuschrist.org url."""
        to_return = super().gen_url()
        # Each url is just an extension on its superclass's url.
        to_return = (
            to_return + "." + str(self.verse_dictionary["verse_number"]) + "?lang=eng#"
        )
        if self.verse_dictionary["verse_number"] == 1:
            return to_return + "p1"
        else:
            return to_return + str(self.verse_dictionary["verse_number"] - 1)


# Unpack JSON-y dicts into objects
scriptures_objects = []
chapters = []
books = []
verses_in_chapters = {}
verses_in_books = {}
biggest_chapter_id = 0
biggest_book_id = 0
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

for verse_dictionary in scriptures:
    new_verse = Verse(verse_dictionary)
    scriptures_objects.append(new_verse)
    books_of_scripture[new_verse.verse_dictionary["volume_id"]].append(new_verse)
    if verse_dictionary["chapter_id"] > biggest_chapter_id:
        verses_in_chapters[verse_dictionary["chapter_id"]] = []
        biggest_chapter_id = verse_dictionary["chapter_id"]
    verses_in_chapters[verse_dictionary["chapter_id"]].append(new_verse)
    if verse_dictionary["book_id"] > biggest_book_id:
        verses_in_books[verse_dictionary["book_id"]] = []
        biggest_book_id = verse_dictionary["book_id"]
    verses_in_books[verse_dictionary["book_id"]].append(new_verse)

for i in range(1, biggest_chapter_id + 1):
    new_chapter = Chapter(i, verses_in_chapters[i])
    chapters.append(new_chapter)

for i in range(1, biggest_book_id + 1):
    new_book = Book(i, verses_in_books[i])
    books.append(new_book)


# Define method
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
        raise ValueError
