import sys
import heapq

a = int(sys.stdin.readline().rstrip())

# 최소 힙 리스트
heap = []
for _ in range(a):
    num = int(sys.stdin.readline().rstrip())
    
    # 0일경우 최소값 출력
    if num == 0:
        if len(heap) ==0:
            print(0)
        else:
            print(heapq.heappop(heap))
    
    else:
        heapq.heappush(heap, num)