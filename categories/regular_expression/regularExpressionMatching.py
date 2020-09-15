def regularExpressionMatching(s, p):
    reg = re.findall(p, s)
    return s == reg[0] if len(reg) > 0 else False
