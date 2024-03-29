import os
import random
import time

import nltk
from nltk.corpus import wordnet as wn

WORDS = []


def pick_word():
    return random.choice(WORDS)


def setup():
    try:
        all_words = wn.words()
        print(">> have wordnet, all is well")
    except LookupError:
        print(">> don't have wordnet, downloading")
        nltk.download('wordnet')
        all_words = wn.words()
    global WORDS
    WORDS = [w for w in all_words if w[0].isalpha() and "_" not in w]


if __name__ == '__main__':
    setup()

    with open('/var/log/randword.log', 'a') as outfile:
        while True:
            outfile.write(pick_word() + os.linesep)

            outfile.flush()
            os.fsync(outfile.fileno())

            time.sleep(1)
