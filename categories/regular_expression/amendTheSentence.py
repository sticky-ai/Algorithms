def amendTheSentence(s):
    f = lambda x: ' ' + x.group().lower()
    p = re.compile('[A-Z]')
    return p.sub(f, s).lstrip()
