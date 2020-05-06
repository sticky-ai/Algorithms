from itertools import permutations

def crosswordFormation(words):
    top, left, right, bottom = [i for i in words]
    cnt = 0

    for i in range(len(top)):
        for j in range(len(left)):
            for k in range(i + 2, len(top)):
                for l in range(len(right)):
                    offset = abs(i - k)
                    
                    if top[i] != left[j] or top[k] != right[l]:
                        continue
                    
                    for m in range(2, len(left)):
                        left_bottom = left[j + m]
                        right_bottom = right[l + m]

                        if not left_bottom or not right_bottom:
                            break
                        
                        for n in range(len(bottom) - offset):
                            if left_bottom == bottom[n] and right_bottom == bottom[n + offset]:
                                cnt += 1
    return cnt
