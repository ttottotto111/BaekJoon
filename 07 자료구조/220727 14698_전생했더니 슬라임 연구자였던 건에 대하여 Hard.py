import sys
import heapq

t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    n = int(sys.stdin.readline().rstrip())
    slime = list(map(int, sys.stdin.readline().rstrip().split()))
    heapq.heapify(slime)
    
    result = 1
    
    if n == 1:
        print(result)
        continue
    
    while len(slime) != 1:
        # 에너지가 가장 적은 슬라임 2마리 합성
        # 합성된 슬라임을 다시 추가
        s1 = heapq.heappop(slime)
        s2 = heapq.heappop(slime)
        
        result *= (s1*s2)
        
        heapq.heappush(slime, s1*s2)
    
    print(result%1000000007)