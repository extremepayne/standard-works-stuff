"""Select a random verse."""
# pylint: disable=C0103
import random_verse

rand_verse = random_verse.get_random_verse()
print("Random verse: ")
print(random_verse.pretty_print_verse(rand_verse))
