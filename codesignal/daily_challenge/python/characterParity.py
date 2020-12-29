def characterParity(symbol):
    try:
        n = int(symbol)
        return 'even' if n % 2 == 0 else 'odd'
    except:
        return 'not a digit'
