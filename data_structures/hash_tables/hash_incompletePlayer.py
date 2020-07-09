from collections import Counter

def solution(participant, completion):
    """Solution 1"""
    return list(Counter(participant) - Counter(completion))[0]

    """Solution 2
    dic = {}
    temp = 0
    
    for p in participant:
        dic[hash(p)] = p
        temp += int(hash(p))
    
    for c in completion:
        temp -= hash(c)
        print(temp)
    
    print(dic)
    """
