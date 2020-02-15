"""Test scriptures module."""
import random_verse


def test_get_random_verse():
    """Make sure it returns a verse."""
    my_random_verse = random_verse.get_random_verse()
    assert isinstance(my_random_verse, dict)
    assert isinstance(my_random_verse["scripture_text"], str)


def test_generate_scripture_url():
    """Make sure the url is generated correctly."""
    verse = {
        "volume_lds_url": "ot",
        "book_lds_url": "ps",
        "chapter_number": 115,
        "verse_number": 7,
    }
    url = "https://www.churchofjesuschrist.org\
/study/scriptures/ot/ps/115.7?lang=eng#6"
    assert random_verse.generate_scripture_url(verse) == url
    verse2 = {
        "volume_lds_url": "bm",
        "book_lds_url": "1-ne",
        "chapter_number": 1,
        "verse_number": 1,
    }
    url2 = "https://www.churchofjesuschrist.org\
/study/scriptures/bofm/1-ne/1.1?lang=eng#p1"
    assert random_verse.generate_scripture_url(verse2) == url2
    verse3 = {
        "volume_lds_url": "dc",
        "book_lds_url": "dc",
        "chapter_number": 6,
        "verse_number": 34,
    }
    url3 = "https://www.churchofjesuschrist.org\
/study/scriptures/dc-testament/dc/6.34?lang=eng#33"
    assert random_verse.generate_scripture_url(verse3) == url3
