def solution(answers):
    s1 = [1, 2, 3, 4, 5] 
    s2 = [2, 1, 2, 3, 2, 4, 2, 5]
    s3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    res = []
    for s in [s1, s2, s3]:
        ls, la = len(s), len(answers)
        s = s * (la // ls) + s[:la % ls]
        cnt = sum(x == y for x, y in zip(answers, s))
        res.append(cnt)
    
    return [i+1 for i in range(len(res)) if res[i] == max(res)]
