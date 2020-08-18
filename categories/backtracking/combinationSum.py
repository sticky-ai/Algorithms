def combinationSum(a, s):
    def backtrack(target, comb, idx):
        if target == 0: # found a valid combination
            res.append(comb)
            
        for i, val in enumerate(a[idx:]):
            if val > target:
                break
            backtrack(target-val, comb + [val], idx + i)

    res = []
    a.sort()
    backtrack(s, [], 0)
    
    return res
