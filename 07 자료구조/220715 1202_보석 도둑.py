import sys
import heapq

# 보석의 개수n, 가방 개수 k
n, k = map(int, sys.stdin.readline().rstrip().split())

# 보석의 무게 m, 가격 v
jewel = []
for _ in range(n):
    m, v = map(int, sys.stdin.readline().rstrip().split())
    heapq.heappush(jewel, [m, v])

# 가방의 무게
bag = []
for _ in range(k):
    heapq.heappush(bag, int(sys.stdin.readline().rstrip()))

# 가방에 담을 수 있는 모든 보석을 추가
bag_jewel = []
price = 0
for _ in range(k):
    weight = heapq.heappop(bag)
    # 가방에 담을 수 있는 모든 보석을 추가
    # 가방을 최소값부터 비교하기때문에 다음 가방에서도 넣을 수 있는 보석 이어서 추출
    while jewel and weight>=jewel[0][0]:
        heapq.heappush(bag_jewel, -heapq.heappop(jewel)[1])
        
    if bag_jewel:
        price += -heapq.heappop(bag_jewel)
    if jewel == False:
        break
    
print(price)