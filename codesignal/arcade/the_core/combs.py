def combs(c1, c2):
    ans = []
    c1 = "-" * (len(c2) - 2) + c1 + "-" * (len(c2) - 2)

    for i in range(len(c1) - (len(c2) - 1)):
        b = "-" * i + c2 + "-" * (len(c1) - len(c2) - i)
        temp = []

        for j, k in zip(c1, b):
            if not (j == "-" and k == "-"): 
                temp.append([j, k])

        if all(j != ["*", "*"] for j in temp): 
            ans.append(temp)

    return min(len(i) for i in ans) if len(ans)>0 else len(c1)-1
