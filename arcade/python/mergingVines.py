def mergingVines(vines, n):
    def nTimes(n):
        return lambda f: lambda x: functools.reduce(lambda x, i: f(x), range(n), x)

    @nTimes(n)
    def sumOnce(vines):
        res = [vines[i] + vines[i + 1] for i in range(0, len(vines) - 1, 2)]
        if len(vines) % 2 == 1:
            res.append(vines[-1])
        return res

    return sumOnce(vines)
