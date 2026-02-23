#!/usr/bin/env python3
def word_count(text):
	num_words = 0
	for word in text.split():
		num_words += 1
	print(f"Found {num_words} total words")

def letter_count(text):
    letters = {}
    for (i, c) in enumerate(text.lower()):
        if c not in letters:
            letters[c] = 1
        if c in letters:
            letters[c] += 1
    print(letters)
