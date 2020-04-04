class Prizes(object):
    def __init__(self, purchase, n, d):
        self.purchase = purchase
        self.n = n
        self.d = d
    def __iter__(self):
        for i, x in enumerate(self.purchase):
            if i % self.n == self.n-1 and x % self.d == 0:
                yield i + 1


def superPrize(purchases, n, d):
    return list(Prizes(purchases, n, d))

