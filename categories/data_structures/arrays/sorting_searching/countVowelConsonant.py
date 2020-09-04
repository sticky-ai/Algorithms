def countVowelConsonant(s):
    v = ['a', 'e', 'i', 'o', 'u']
    return sum(1 if c in v else 2 for c in s)
