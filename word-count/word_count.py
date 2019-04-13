import re
from collections import Counter

words = re.compile("[a-z0-9]+(['][a-z]+)?")

def word_count(phrase):
    return Counter(word.group(0) for word in words.finditer(phrase.lower()))
