def solution(p, l):
    q = [(i, p) for i, p in enumerate(p)]
    cnt = 0
    
    while True:
        cur = q.pop(0)
        if any(cur[1] < i[1] for i in q):
            q.append(cur)
        else:
            cnt += 1
            if cur[0] == l:
                return cnt
