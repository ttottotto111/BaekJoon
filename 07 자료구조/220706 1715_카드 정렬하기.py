import sys
import heapq

n = int(sys.stdin.readline().rstrip())

num = []

for _ in range(n):
    heapq.heappush(num, int(sys.stdin.readline().rstrip()))

# 카드가 1개일경우
if len(num) == 1:
    print(0)
else:
    result = 0
    while len(num)>1:
        # 가장작은 카드덱 2개를 가져옴
        card = heapq.heappop(num) + heapq.heappop(num)
        # 비교횟수 카운트
        result += card
        # 합친 덱을 다시 힙에 넣음
        heapq.heappush(num, card)
        
    print(result)