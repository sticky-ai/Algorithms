def hangman(word, letters):
    s = list(set(word))
    cnt = 0
    for l in letters:
        if l in s:
            s.remove(l)
            if len(s) == 0:
                if cnt >= 6:
                    return False
                else:
                    return True
        else:
            cnt += 1
    
    if len(s) != 0:
        return False
