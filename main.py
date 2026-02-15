#!/usr/bin/env python3
path_to_file = "books/frankenstein.txt"
def get_book_text(path_to_file):
	with open(path_to_file) as f:
		contents = f.read()
	return contents
def main():
	text = get_book_text(path_to_file)
	print(text)
main()