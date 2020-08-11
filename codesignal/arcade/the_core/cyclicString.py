def cyclicString(s):
    for i in range(len(s)):
        sub = s[:i+1]
        repeat = len(s) // (i+1) + 1
        if s in sub * repeat:
            return i + 1
