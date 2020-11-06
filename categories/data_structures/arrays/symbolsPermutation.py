from collections import Counter

def symbolsPermutation(word1, word2):
    return Counter(word1) == Counter(word2)
