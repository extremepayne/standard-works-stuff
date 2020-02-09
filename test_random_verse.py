"""Tests scriptures module."""
import scripture


def test_get_random_verse():
    """Tests scripture.get_random_verse() function."""
    my_random_verse = scripture.get_random_verse()
    assert my_random_verse != ""
