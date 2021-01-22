def textJustification(words, l):
    ans, cur, curlen = [], [], 0

    for w in words:
        if curlen + len(w) + len(cur) > l:
            spacelen = l - curlen
            words_amount = len(cur) - 1 or 1
            for i in range(spacelen):
                print(i % words_amount)
                cur[i % words_amount] += ' '
            
            ans.append(''.join(cur))
            cur, curlen = [], 0
            
        cur += [w]
        curlen += len(w)
        
    return ans + [' '.join(cur).ljust(l)]
