"""The underlying methods to get a random verse."""
# pylint: disable=C0103
import json
import random
import textwrap

file_path = "lds-scriptures.json"


def get_random_verse():
    """Produce a random verse."""
    with open(file_path, "r") as scripture_file:
        file_list = scripture_file.readlines()
        length_of_file = len(file_list)
        verse_number = random.randint(0, length_of_file)
        verse_json = file_list[verse_number]
        verse = json.loads(verse_json)
    return verse


def pretty_print_verse(verse):
    """Given a verse in dictionary form, return a nice-looking string."""
    to_return = verse["verse_title"]
    to_return += ": \n"
    wrapped_verse = textwrap.wrap(verse["scripture_text"])
    for line in wrapped_verse:
        to_return += line + "\n"
    to_return += generate_scripture_url(verse)
    return to_return


def generate_scripture_url(verse):
    """Generates a verse's churchofjesuschrist url."""
    to_return = "https://www.churchofjesuschrist.org/study/scriptures/"
    if verse["volume_lds_url"] == "bm":
        to_return += "bofm"
    elif verse["volume_lds_url"] == "dc":
        to_return += "dc-testament"
    else:
        to_return += verse["volume_lds_url"]
    to_return += "/" + verse["book_lds_url"]
    to_return += "/" + str(verse["chapter_number"])
    to_return = (
        to_return + "." + str(verse["verse_number"]) + "?lang=eng#"
        )
    if verse["verse_number"] == 1:
        return to_return + "p1"
    return to_return + str(verse["verse_number"] - 1)
