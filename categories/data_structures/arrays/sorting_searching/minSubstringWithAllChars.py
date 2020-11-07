def minSubstringWithAllChars(s, t):
    for i in range(len(s) + 1):
        for j in range(len(s) - i + 1):
            c = filter(lambda x: x in t, s[j:j+i])
            if len(set(c)) == len(t):
                return s[j:j+i]
    return ''
