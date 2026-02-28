#!/usr/bin/env python3
from stats import word_count, letter_count
def main():
    path_to_file = "books/frankenstein.txt"
    text = get_book_text(path_to_file)
    words = word_count(text)
    letters = letter_count(text)
    print_report(path_to_file, words, chars_list)

def get_book_text(path_to_file):
	with open(path_to_file) as f:
		contents = f.read()
	return contents

def print_report(path_to_file, words, chars_list):
    print("======== BOOKBOT ========")
    print(f"Analyzing book found at {path_to_file}...")
    print("-------- Word Count --------")
    print(f"Found {words} total words")
    print("-------- Character Count --------")
    for item in chars_list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")

    print("======== END ========")

main()
