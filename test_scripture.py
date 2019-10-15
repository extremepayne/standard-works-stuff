import scripture
import pytest


def test_sciptures():
    assert scripture.scriptures[1] == {
        "volume_id": 1,
        "book_id": 1,
        "chapter_id": 1,
        "verse_id": 2,
        "volume_title": "Old Testament",
        "book_title": "Genesis",
        "volume_long_title": "The Old Testament",
        "book_long_title": "The First Book of Moses called Genesis",
        "volume_subtitle": "",
        "book_subtitle": "",
        "volume_short_title": "OT",
        "book_short_title": "Gen.",
        "volume_lds_url": "ot",
        "book_lds_url": "gen",
        "chapter_number": 1,
        "verse_number": 2,
        "scripture_text": "And the earth was without form, \
and void; and darkness was upon \
the face of the deep. And the Spirit of God \
moved upon the face of the waters.",
        "verse_title": "Genesis 1:2",
        "verse_short_title": "Gen. 1:2",
    }


def test_get_random_verse():
    my_random_verse = scripture.get_random_verse()
    assert isinstance(my_random_verse, scripture.Verse)
    assert "scripture_text" in my_random_verse.verse_dictionary
    assert my_random_verse.text != ""
    with pytest.raises(ValueError):
        my_random_verse = scripture.get_random_verse(17.2)
    my_volume = 1
    my_random_verse = scripture.get_random_verse(my_volume)
    assert my_random_verse.verse_dictionary["volume_id"] == my_volume


def test_chapter_printing():
    my_chapter = scripture.chapters[0]
    print(my_chapter)
    assert my_chapter.ch_id == 1


def test_book_printing():
    my_book = scripture.books[0]
    print(my_book)
    assert my_book.bk_id == 1


def test_volume_printing():
    my_volume = scripture.volumes[0]
    print(my_volume)
    assert my_volume.vol_id == 1
