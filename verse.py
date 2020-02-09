"""Select a random verse."""
# pylint: disable=C0103
import scripture

rand_verse = scripture.get_random_verse()
print("Random verse: ")
print(scripture.pretty_print_verse(rand_verse))
