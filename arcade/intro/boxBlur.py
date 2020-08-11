def boxBlur(m):
    rows = len(m)
    cols = len(m[0])
    result = []

    for i in range(1, rows-1):
        row=[]
        for j in range(1, cols-1):
            row.append(sum([m[i+k][j+l] for k in [-1,0,1] for l in [-1,0,1]])//9)
        result.append(row)
    return result
