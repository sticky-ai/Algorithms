def removeDuplicateAdjacent(s):
    p = re.sub(r'([a-z])\1+', '', s)
    return s if p == s else removeDuplicateAdjacent(p)
