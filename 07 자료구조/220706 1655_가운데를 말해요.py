import sys
import heapq

n = int(sys.stdin.readline().rstrip())

# 작은수를 넣을 힙 (최대힙)
# 최대힙으로 넣어야 맨앞자리가 중간값으로 고정 (작은수중 가장 큰수가 중간값)
small = []
# 큰수를 넣을 힙 (최소힙)
big = []

for _ in range(n):
    x = int(sys.stdin.readline().rstrip())

    # 길이가 같을경우 작은수를 넣을 힙에 추가 (두개의 힙의 크기를 맞춰준다)
    if len(small) == len(big):
        heapq.heappush(small, -x)
    else:
        heapq.heappush(big, x)
        
    # 큰수가 작은수 힙에 들어왔을경우
    # 큰수 힙의 가장작은수와, 작은수 힙의 가장 큰수를 교환
    # big[0] 큰수중 가장 작은수, small[0] 작은수중 가장큰수(최대 힙이기때문)
    if big and big[0]< -small[0]:
        s = heapq.heappop(small)
        b = heapq.heappop(big)
        
        heapq.heappush(small, -b)
        heapq.heappush(big, -s)
    
    print(-small[0])