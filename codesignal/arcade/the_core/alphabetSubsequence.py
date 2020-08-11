def alphabetSubsequence(s):
    return s == ''.join(sorted(s)) and len(set(s)) == len(s)
