def reverse(text):
    l = []
    for letter in text:
        l.append(letter)
    return "".join(l[::-1])
