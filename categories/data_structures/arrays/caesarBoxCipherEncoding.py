def caesarBoxCipherEncoding(s):
    sqrt = int(len(s) ** 0.5)
    res = zip(*[s[i:i+sqrt] for i in range(0, len(s), sqrt)])
    return ''.join(''.join(r) for r in res)
