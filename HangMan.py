import random

from Words import wordlist


def get_word():
    word = random.choice(wordlist)
    return word.upper()


def play(word):
    word_completion = "_" * len(word)

