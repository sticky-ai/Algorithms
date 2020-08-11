from itertools import product

def crackingPassword(digits, k, d):
    def createNumber(digs):
        return "".join(map(str, digs))

    return sorted(x for x in map(createNumber,product(digits,repeat=k)) if int(x)%d==0)

