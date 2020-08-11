def characterParity(symbol):
    try:
        if int(symbol) % 2 == 0: return 'even'
        else: return 'odd'
    except:
        return 'not a digit'
