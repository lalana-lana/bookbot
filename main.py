#!/usr/bin/env python3
import sys
from stats import (
    word_count,
    sorted_letters,
    letter_count)

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    text = get_book_text(path)
    words = word_count(text)
    letters = letter_count(text)
    chars_list = sorted_letters(letters)
    print_report(sys.argv[1], words, chars_list)

def get_book_text(path):
	with open(path) as f:
		return f.read()

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
