def hangman(word, letters):
    s = list(set(word))
    cnt = 0
    for l in letters:
        if l in s:
            s.remove(l)
            if len(s) == 0:
                return False if cnt >= 6 else True
        else:
            cnt += 1
    
    return False if len(s) != 0 else True
