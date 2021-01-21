def factorialTrailingZeros(n):
    return len(re.findall('0+$', str(math.factorial(n)))[0])
