def hangman(word, letters):
    ans = ['0'] * len(word)
    cnt = 0
    
    for l in letters:
        if cnt >= 6: return False
        
        if l in word:
            idxs = [i for i in range(len(word)) if word[i] == l]
            for idx in idxs:
                ans[idx] = word[idx]
        else:
            cnt += 1
        
    return ''.join(ans) == word
