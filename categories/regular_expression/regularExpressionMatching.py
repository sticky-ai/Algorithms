def regularExpressionMatching(s, p):
    return s in re.findall(p, s)
    #return True if re.search('^' + p + '$', s) else False
    
