def is_pangram(sentence):
    chars = list(sentence.lower())
    charset = set()
    for c in chars:
        if c.isalpha():
            charset.add(c)
    return len(charset) == 26
