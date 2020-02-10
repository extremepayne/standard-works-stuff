"""Test scriptures module."""
import random_verse


def test_get_random_verse():
    """Tests scripture.get_random_verse() function."""
    my_random_verse = random_verse.get_random_verse()
    assert my_random_verse != ""
