# import scripture
# from textwrap import wrap


# def ask(prompt, type_=None, min_=None, max_=None, range_=None):
#     """Get user input of a certain type, with range and min/max options."""
#     """From stackoverflow 23294658"""
#     if min_ is not None and max_ is not None and max_ < min_:
#         raise ValueError("min_ must be less than or equal to max_.")
#     while True:
#         ui = input(prompt)
#         if type_ is not None:
#             try:
#                 ui = type_(ui)
#             except ValueError:
#                 print("Input type must be {0}.".format(type_.__name__))
#                 continue
#         if max_ is not None and ui > max_:
#             print("Input must be less than or equal to {0}.".format(max_))
#         elif min_ is not None and ui < min_:
#             print("Input must be greater than or equal to {0}.".format(min_))
#         elif range_ is not None and ui not in range_:
#             if isinstance(range_, range):
#                 template = "Input must be between {0.start} and {0.stop}."
#                 print(template.format(range_))
#             else:
#                 template = "Input must be {0}."
#                 if len(range_) == 1:
#                     print(template.format(*range_))
#                 else:
#                     print(
#                         template.format(
#                             " or ".join(
#                                 (", ".join(map(str, range_[:-1])), str(range_[-1]))
#                             )
#                         )
#                     )
#         else:
#             return ui


# print("Choose from the list below: ")
# volume_urls = {}
# for vol in scripture.books_of_scripture:
#     print(vol, end=":\t")
#     print(scripture.books_of_scripture[vol][0]["volume_title"])
#     volume_urls.update({vol: scripture.books_of_scripture[vol][0]["volume_lds_url"]})
# volume = ask("Pick one: ", type_=int, min_=1, max_=5)

# i = 0
# books_in_vol = []
# books_in_vol_url = []
# for verse in scripture.books_of_scripture[volume]:
#     if verse["book_lds_url"] not in books_in_vol_url:
#         books_in_vol_url.append(verse["book_lds_url"])
#         books_in_vol.append(verse["book_title"].lower())

# print("Choose from the lsit below:")
# books_string = ""
# for book in books_in_vol:
#     if len(book) < 10:
#         books_string += book + "\t\t"
#     else:
#         books_string += book + "\t"
# for line in wrap(books_string):
#     print(line)
# book = ask("Choice: ", type_=str, range_=books_in_vol)
# chapter = ask("Input a chapter: ", type_=int, min_=1)
# url_dictionary = {
#     "volume_lds_url": str(volume),
#     "book_lds_url": book,
#     "chapter_number": chapter,
# }
# url = scripture.generate_scripture_url(url_dictionary, chapter=True)
# print(url)
# # print(books_in_vol_url)
# # print(volume_urls)
