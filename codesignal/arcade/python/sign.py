class Functions(object):
    @staticmethod
    def sign(x):
        if x == 0: return 0
        elif x < 0: return -1
        else: return 1

def sign(x):
    return Functions.sign(x)

