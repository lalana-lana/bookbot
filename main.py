#!/usr/bin/env python3
from stats import word_count
path_to_file = "books/frankenstein.txt"
def get_book_text(path_to_file):
	with open(path_to_file) as f:
		contents = f.read()
	return contents