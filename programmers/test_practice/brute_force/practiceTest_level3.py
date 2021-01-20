def solution(brown, yellow):
    b, y = brown, yellow
    x = (b + 4 + ((b + 4) ** 2 - 4 ** 2 * (b + y)) ** 0.5) / 4
    y = (b + y) // x
    return [max(x, y), min(x, y)]
