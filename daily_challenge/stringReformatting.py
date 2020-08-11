def stringReformatting(s, k):
    s = re.sub('-', '', s)
    if len(s) % k == 0:
        return '-'.join([s[i:i+k] for i in range(0, len(s), k)])
    else:
        temp = [s[:len(s) % k]]
        for i in range(len(s) % k,  len(s), k):
            temp.append(s[i:i+k])
        return '-'.join(temp)
