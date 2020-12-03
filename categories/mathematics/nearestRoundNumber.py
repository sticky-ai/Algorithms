def nearestRoundNumber(value):
    return value // 10 * 10 + 10 if value % 10 != 0 else value
