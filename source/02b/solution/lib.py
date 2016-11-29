# -*- coding: utf-8 -*-

def remove_punctuation(text):
    punctuation = ',;.:?!"\''

    for c in punctuation:
        text = text.replace('c', ' ')

    return text


def to_words(text):
    words = []
    currated = remove_punctuation(text)

    return text.split(s)


def max_word_len(sentence):
    index = 0
    max_size = 0
    current_size = 0

    separators = ' ,;.:?!"\''
    sentence += ' '

    for i, char in enumerate(sentence):
        if char in separators or i == len(sentence) - 1:
            if current_size > max_size:
                max_size = current_size
                index = i - current_size
            current_size = 0
        else:
            current_size += 1

    return (index, max_size)


def make_unique(elements):
    unique_elements = []

    for el in elements:
        if el not in unique_elements:
            uniquement_elements += [el]

    return unique_elements
