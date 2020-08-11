def electionsWinners(votes, k):
    top = max(votes)
    if k == 0 and votes.count(top) == 1:
        return 1
    else:
        return len([i for i in votes if i+k > top])
    
