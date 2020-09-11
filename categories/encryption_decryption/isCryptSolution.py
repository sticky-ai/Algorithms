def isCryptSolution(crypt, solution):
    d = {k:v for k, v in solution}
    
    arr = []
    for c in crypt:
        temp = ''
        for i in c:
            temp += str(d[i])
        
        if temp[0] == '0' and len(temp) > 1:
            return False
            
        arr.append(int(temp))
    
    return True if arr[0] + arr[1] == arr[2] else False
