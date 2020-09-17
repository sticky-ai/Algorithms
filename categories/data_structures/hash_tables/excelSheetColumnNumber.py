def excelSheetColumnNumber(s):
    chars = string.ascii_uppercase
    dic = {v:k for k, v in zip(range(1, len(chars) + 1), chars)}
    return sum((26 ** i) * dic[c] for i, c in zip(range(len(s) - 1, -1, -1), s))
