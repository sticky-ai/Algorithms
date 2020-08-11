def increaseNumberRoundness(n):
    n = str(n)
    arr = []
    for i in range(1, len(n)):
        if int(n[i-1]) == 0 and int(n[i]) > 0:
            return True
    return False
