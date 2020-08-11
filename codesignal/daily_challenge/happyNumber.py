def happyNumber(n):
    s = sum([int(num) ** 2for num in str(n)])
    
    try:
        if s == 1:
            return True
        else:
            return happyNumber(s)
    except:
        return False
