import heapq

def solution(scoville, K, cnt = 0):
    heap = []
    for s in scoville:
        heapq.heappush(heap, s)
        
    while heap[0] < K:
        try:
            heapq.heappush(heap, heapq.heappop(heap) + heapq.heappop(heap) * 2)
        except:
            return -1
        cnt += 1
    return cnt
