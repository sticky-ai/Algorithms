def strstr(s, x):
    p = re.search(x, s)
    return p.start() if p else -1
