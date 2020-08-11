def leastFactorial(n):
    return min([math.factorial(i) for i in range(6) if math.factorial(i) >= n])


