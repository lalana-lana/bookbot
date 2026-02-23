#!/usr/bin/env python3
from stats import word_count, letter_count
def main():
    path_to_file = "books/frankenstein.txt"
    text = get_book_text(path_to_file)
    words = word_count(text)
    letters = letter_count(text)

def get_book_text(path_to_file):
	with open(path_to_file) as f:
		contents = f.read()
	return contents

main()
