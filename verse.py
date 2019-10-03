"""select a random verse"""
# pylint: disable=C0103
import scripture
from textwrap import wrap

rand_verse = scripture.get_random_verse()
print("Random verse: ")
print(rand_verse)
