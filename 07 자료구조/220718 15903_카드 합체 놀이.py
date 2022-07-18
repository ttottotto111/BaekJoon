import sys
import heapq

n, m = map(int, sys.stdin.readline().rstrip().split())

card_list = list(map(int, sys.stdin.readline().rstrip().split()))

card = []
for c in card_list:
    heapq.heappush(card, c)

for _ in range(m):
    a = heapq.heappop(card)
    b = heapq.heappop(card)
    s = a+b
    
    heapq.heappush(card, s)
    heapq.heappush(card, s)

print(sum(card))