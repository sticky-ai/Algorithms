def isCorrect(c):
    cnt = 0
    for i in range(len(c)):
        cnt = cnt + 1 if c[i] == '(' else cnt - 1
        if cnt < 0:
            return False
    return True
    
def isBalanced(c):
    return c.count('(') == c.count(')')

def solution(p):
    u, v = [], []
    if isCorrect(p):
        return p
    
    for i in range(2, len(p) + 1, 2):
        if isBalanced(p[:i]):
            u, v = p[:i], p[i:]
            break
        
    if isCorrect(u):
        return u + solution(v)
    
    else:
        return '(' + solution(v) + ')' + u[1:len(u)-1].replace('(','0').replace(')', '(').replace('0',')')
    
