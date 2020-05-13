def houseOfCats(legs):
    return sorted([(legs - (i * 4)) / 2 for i in range(legs // 4 + 1)])

