from collections import Counter

def createAnagram(s, t):
    return len(list((Counter(s) - Counter(t)).elements()))

