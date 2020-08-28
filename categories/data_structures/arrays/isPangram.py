def isPangram(sentence):
    sentence = sentence.lower()
    for s in string.ascii_lowercase:
        if s not in sentence:
            return False
    return True
