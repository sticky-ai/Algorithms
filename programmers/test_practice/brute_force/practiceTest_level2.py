from itertools import permutations

def isPrime(n):
    if n < 2: return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True    

def solution(numbers):
    s = set()
    for i in range(1, len(numbers) + 1):        
        for p in set(permutations(numbers, i)):
            p = int(''.join(p))
            if isPrime(p):
                s.add(p)
    return len(s)
        
        
