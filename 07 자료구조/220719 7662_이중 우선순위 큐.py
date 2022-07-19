import sys
import heapq

t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    # 최소값 큐
    small = []
    # 최대값 큐
    big = []
    
    k = int(sys.stdin.readline().rstrip())
    
    # 제거 여부
    delete = [False]*(k+1)
    
    for i in range(k):
        order, num = map(str, sys.stdin.readline().rstrip().split())

        if order == "I":
            heapq.heappush(small, (int(num), i))
            heapq.heappush(big, (-int(num), i))
            delete[i] = True
            
        elif order == "D":
            if len(small) ==0 or len(big) == 0:
                continue
            # 최대값 추출
            if int(num) == 1:
                # 최대값 큐에서 최소값에서 제거된 항목 제거
                while big and delete[big[0][1]] == False:
                    heapq.heappop(big)
                # 최대값 추출
                if big:
                    delete[big[0][1]] = False
                    heapq.heappop(big)
            # 최소값 추출
            if int(num) == -1:
                # 최소값 큐에서 최대값에서 제거된 항목 제거
                while small and delete[small[0][1]] == False:
                    heapq.heappop(small)
                # 최소값 추출
                if small:
                    delete[small[0][1]] = False
                    heapq.heappop(small)
                    
    # 출력전 제거된값 확인
    while big and delete[big[0][1]] == False:
        heapq.heappop(big)    
    while small and delete[small[0][1]] == False:
        heapq.heappop(small)

    if len(small) == 0:
        print("EMPTY")
    else:
        print(-heapq.heappop(big)[0], end=" ")
        print(heapq.heappop(small)[0])