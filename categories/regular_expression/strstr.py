def strstr(s, x):
    p = re.search(x, s)
    return -1 if p == None else p.span()[0]
