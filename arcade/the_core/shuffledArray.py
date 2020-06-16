def shuffledArray(shuffled):
    for i in range(len(shuffled)):
        s = [shuffled[j] for j in range(len(shuffled)) if j != i]
        if sum(s) == shuffled[i]:
            return sorted(s)
            
