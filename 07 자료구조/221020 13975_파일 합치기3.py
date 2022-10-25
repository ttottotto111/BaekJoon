import sys
import heapq

t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    n = int(sys.stdin.readline().rstrip())
    file_list = list(map(int,sys.stdin.readline().rstrip().split()))
    heapq.heapify(file_list)
    
    result = 0
    
    while len(file_list) > 1:
        file = heapq.heappop(file_list) + heapq.heappop(file_list)
        result += file
        heapq.heappush(file_list, file)
    
    print(result)