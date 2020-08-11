def pairOfShoes(shoes):
    for i in shoes:
        if i[0] == 0:
            if shoes.count(i) != shoes.count([i[0]+1, i[1]]):
                return False
        elif i[0] == 1:
            if shoes.count(i) != shoes.count([i[0]-1, i[1]]):
                return False
    return True
