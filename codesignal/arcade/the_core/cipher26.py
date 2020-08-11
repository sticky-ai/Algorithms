import string
def cipher26(message):
    alpha = string.ascii_lowercase
    answer = ''
    temp = 0

    for i, j in enumerate(message):
        answer += alpha[(alpha.find(j) - temp) % 26]
        temp += (alpha.find(j) - temp) % 26
    return answer
