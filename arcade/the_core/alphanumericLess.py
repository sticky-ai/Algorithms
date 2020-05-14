def get_tokens(s):
    temp = '0'
    tokens = []
    for i in s:
        if i.isdigit():
            temp += i
        else:
            if temp != '0':
                tokens.append(temp)
                temp = '0'
            tokens.append(i)
    tokens.append(temp)
    return tokens


def alphanumericLess(s1, s2):
    t1, t2 = get_tokens(s1), get_tokens(s2)
    print(t1, t2)
    for x, y in zip(t1, t2):
        if x.isdigit():
            if y.isalpha():
                return True
            else:
                if int(x) < int(y):
                    return True
                elif int(x) > int(y):
                    return False
        else:
            if y.isdigit():
                return False
            else:
                if x < y:
                    return True
                elif x > y:
                    return False
                    
    if len(t1) < len(t2):
        return True
    elif len(t1) > len(t2):
        return False
    
    
    for x,y in zip(t1, t2):
        if x.isdigit():
            if x.count('0') > y.count('0'):
                return True
            elif x.count('0') < y.count('0'):
                return False
    return False
