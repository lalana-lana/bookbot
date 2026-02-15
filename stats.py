#!/usr/bin/env python3
def word_count(get_book_text):
	contents = get_book_text("books/frankenstein.txt")
	num_words = 0
	for word in contents.split():
		num_words += 1
	print(f"Found {num_words} total words")