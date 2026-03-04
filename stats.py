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
    return letters

def letter_sort(dict):
    return dict["num"]

def sorted_letters(letters):
    sorted_list = []
    for c in letters:
        sorted_list.append({"char": c, "num": letters[c]})
    sorted_list.sort(reverse=True, key=letter_sort)
    return sorted_list
