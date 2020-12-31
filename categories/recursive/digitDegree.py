def digitDegree(n, cnt = 0):
    if len(str(n)) == 1:
        return cnt 
    else:
        cnt += 1
        return digitDegree(sum(map(int, str(n))), cnt)
