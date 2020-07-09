def solution(h):
    answer = [0] * len(h)
    print(answer)
    for i in range(len(h) -1, 0, -1):
        for j in range(i-1, -1, -1):
            if h[i] < h[j]:
                answer[i] = j+1
                break
    return answer
