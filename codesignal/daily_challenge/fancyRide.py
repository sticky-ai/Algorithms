L, F = eval(dir()[0])
g = max(i for i, f in enumerate(F) if f * L <= 20)
if g == 0: return 'UberX'
if g == 1: return 'UberXL'
if g == 2: return 'UberPlus'
return 'UberBlack' if g == 3 else 'UberSUV'
    
    
# 173 chars
# def fancyRide(l, fares):
    # g = max(i for i, f in enumerate(fares) if f * l <= 20)
    # if g == 0: return 'UberX'
    # if g == 1: return 'UberXL'
    # if g == 2: return 'UberPlus'
    # if g == 3: return 'UberBlack'
    # if g == 4: return 'UberSUV'
