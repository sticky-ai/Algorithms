i = eval(dir()[0])[0]
if max(ord(s) - 97 for s in i) + 1 != len(set(i)):
    return False

c = [i.count(s) for s in sorted(set(i))]
for j in range(len(c) - 1):
    if c[j] < c[j+1]:
        return False
return True

# def isBeautifulString(inputString):
#     # m = max(ord(s) - 97 for s in inputString) + 1
#     # if m != len(set(inputString)): return False
#     # cnt = [inputString.count(s) for s in sorted(set(inputString))]
#     # for i in range(len(cnt)-1):
#     #     if cnt[i] < cnt[i+1]:
#     #         return False
#     # return True
    
    
    
