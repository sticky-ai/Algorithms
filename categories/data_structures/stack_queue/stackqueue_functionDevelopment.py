from math import ceil

def solution(progresses, speeds):
    m = list(zip(progresses, speeds))
    fin = [ceil((100-p)/s) for p, s in m]
    
    cnt = 1
    answer = []
    
    for i in range(len(fin)):
        try:
            if fin[i] < fin[i+1]:
                answer.append(cnt)
                cnt = 1
            else:
                fin[i+1] = fin[i]
                cnt += 1
        except IndexError:
            answer.append(cnt)
    
    return answer
