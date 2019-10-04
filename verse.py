"""select a random verse"""
# pylint: disable=C0103
import scripture

rand_verse = scripture.get_random_verse()
print("Random verse: ")
print(rand_verse.verse_dictionary)
