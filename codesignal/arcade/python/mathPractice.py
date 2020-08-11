def mathPractice(numbers):
    return functools.reduce(lambda i,x: (i+x[1] if x[0]%2 else i*x[1]), enumerate(numbers), 1)
