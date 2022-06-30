import sys
import heapq

a = int(sys.stdin.readline().rstrip())

# 최대 힙을 위한 힙 구현
heap = []
for _ in range(a):
    num = int(sys.stdin.readline().rstrip())
    
    # 0 입력시 출력
    if num == 0:
        if len(heap) ==0:
            print(0)
        else:
            print(abs(heapq.heappop(heap)))
    
    else:
        heapq.heappush(heap, -num)