def electionsWinners(votes, k):
    top = max(votes)
    if k == 0 and votes.count(top) == 1:
        return 1    
    return len([v for v in votes if v + k > top])
