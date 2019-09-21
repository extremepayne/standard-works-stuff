"""select a random verse"""
# pylint: disable=C0103
import scripture
from textwrap import wrap

rand_verse = scripture.get_random_verse()
print("Random verse: ")
wrapped_verse = wrap(rand_verse["scripture_text"])
print(rand_verse["verse_title"], end=": ")
for line in wrapped_verse:
    print(line)
print(scripture.generate_churchofjesuschrist_url(rand_verse))

# rand_verse = get_random_verse(3)  # from the book of mormon
# print("\nRandom verse, but only from the book of mormon: ")
# print(rand_verse["verse_title"], rand_verse["scripture_text"], sep=': ')
