def findSubstrings(words, parts):
    output = []
    
    for w in words:
        longest = 0
        match   = ""
        position = len(w)

        for p in parts:
    
            if p in w:
    
                if len(p) > longest or (len(p) == longest and w.index(p) < position):
                    longest = len(p)
                    match = p
                    position = w.index(p)

        if longest > 0:
            loc = w.index(match)
            output.append(w[:loc] + "[" + match + "]" + w[loc + len(match):])
            
        else:
            output.append(w)
            
    return output
