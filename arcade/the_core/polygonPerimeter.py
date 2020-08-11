def polygonPerimeter(m):
    # if a cell is true, count bordering cells that are False or out of bound as perimeter.
    # only check cells immediately adjacent (not diagonal)
    
    rb = len(m)
    cb = len(m[0])
    p = 0
    for r in range(rb):
        for c in range(cb):
            if m[r][c]:
                p += bound_check(m,r-1,c,rb,cb) # up
                p += bound_check(m,r,c+1,rb,cb) # down
                p += bound_check(m,r,c-1,rb,cb) # left
                p += bound_check(m,r+1,c,rb,cb) # right
    return p

def bound_check(m,r,c,rb,cb):
    if (r >= 0 and c >= 0 and r < rb and c < cb) and m[r][c]:
        # if we're in bounds and True, then don't Add to perim.
        return 0
    else:
        # otherwise we are out of bounds OR in bounds and False.  Add.
        return 1
