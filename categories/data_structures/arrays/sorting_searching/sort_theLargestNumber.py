from functools import cmp_to_key

def comparator(x, y):
    n1 = x + y
    n2 = y + x
    if n1 > n2:
        return 1
    else:
        return -1

    
def solution(numbers):
    n = [str(i) for i in numbers]
    answer = list(sorted(n, key=cmp_to_key(comparator), reverse=True))
    return str(int(''.join(answer)))
    
    
