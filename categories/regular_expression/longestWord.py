def longestWord(text):
    return max(re.findall('[a-zA-Z]+', text), key = len)
