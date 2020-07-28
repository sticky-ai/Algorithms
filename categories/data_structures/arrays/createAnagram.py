from collections import Counter

def createAnagram(s, t):
    return sum((Counter(s) - Counter(t)).values())
