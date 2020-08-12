def amendTheSentence(s):
    f = lambda x: ' ' + x.group().lower()
    p = re.compile('[A-Z]')
    return p.sub(f, s).lstrip()

# def amendTheSentence(s):
#     sp = [n for n in re.split('([A-Z]{1}[a-z]*)', s) if n != '']
#     return ' '.join(sp).lower()
