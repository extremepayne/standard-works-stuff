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
        "volume_id": 1,
        "book_id": 19,
        "chapter_id": 593,
        "verse_id": 15838,
        "volume_title": "Old Testament",
        "book_title": "Psalms",
        "volume_long_title": "The Old Testament",
        "book_long_title": "The Book of Psalms",
        "volume_subtitle": "",
        "book_subtitle": "",
        "volume_short_title": "OT",
        "book_short_title": "Ps.",
        "volume_lds_url": "ot",
        "book_lds_url": "ps",
        "chapter_number": 115,
        "verse_number": 7,
        "scripture_text": "They have hands, but they handle not: feet have they, but they walk not: neither speak they through their throat.",
        "verse_title": "Psalms 115:7",
        "verse_short_title": "Ps. 115:7",
    }
