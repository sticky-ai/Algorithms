def leastCommonPrimeDivisor(a, b):
    
    def isPrime(n):
        for i in range(2, n):
            if n % i == 0:
                return False
        return True
    
    a_list = [i for i in range(2, a+1) if a % i == 0 and isPrime(i)]
    b_list = [i for i in range(2, b+1) if b % i == 0 and isPrime(i)]
    
    for n in a_list:
        if n in b_list:
            return n
    return -1
