def isSentenceCorrect(sentence):
    pattern = re.compile('^[A-Z][^.?!]*[.?!]$')
    return re.match(pattern, sentence) is not None

