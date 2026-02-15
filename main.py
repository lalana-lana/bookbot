#!/usr/bin/env python3
path_to_file = "books/frankenstein.txt"
def get_book_text(path_to_file):
	with open(path_to_file) as f:
		file.contents = f.read(path_to_file)
	return f.read
def main():
	text = get_book_text(path_to_file)
	print(text)
main()