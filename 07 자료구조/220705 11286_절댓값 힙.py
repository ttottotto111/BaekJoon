import sys
import heapq

n = int(sys.stdin.readline().rstrip())

heap = []

for _ in range(n):
    # (절대값, 수) 형태로 저장
    x = int(sys.stdin.readline().rstrip())
    
    # 0이 아닐경우 입력
    if x != 0:
        heapq.heappush(heap, (abs(x), x))
    # 0일경우 출력
    else:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap)[1])