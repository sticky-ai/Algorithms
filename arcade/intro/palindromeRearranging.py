def palindromeRearranging(inputString):
    lst = []

    # 인풋값의 길이가 짝수일 때
    if len(inputString) == 1:
        return True

    elif len(inputString) % 2 == 0:
        for i in inputString:
            if inputString.count(i) % 2 != 0:
                return False
        else:
            return True

    # 인풋값의 길이가 홀수일 때
    else:
        for i in inputString:
            if inputString.count(i) % 2 != 0:
                if i in lst:
                    continue
                else:
                    lst.append(i)
        return len(lst) == 1

