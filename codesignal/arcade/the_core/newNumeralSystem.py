def newNumeralSystem(number):
    pure = ord(number) - 65
    perms = [(i, pure - i) for i in range(int(pure / 2 + 1)) if i + (pure - i) == pure]
    return ['{} + {}'.format(chr(i+65), chr(j+65)) for i, j in perms]
