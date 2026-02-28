#!/usr/bin/env python3
def word_count(text):
	num_words = 0
	for word in text.split():
		num_words += 1
	return num_words

def letter_count(text):
    letters = {}
    for (i, c) in enumerate(text.lower()):
        if c not in letters:
            letters[c] = 0
        if c in letters:
            letters[c] += 1
    print(letters)

def letter_sort(dict):
    return dict["num"]
