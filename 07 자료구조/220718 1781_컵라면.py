import sys
import heapq

n = int(sys.stdin.readline().rstrip())

num = []

for _ in range(n):
    deadline, cup = map(int, sys.stdin.readline().rstrip().split())
    num.append((deadline, cup))

num.sort()

queue = []

for deadline, cup in num:
    # 컵라면을 큐에 넣음
    heapq.heappush(queue, cup)
    # 만약 데드라인이 큐의 크기보다 작을경우(문제를 푼 시점이 데드라인을 초과할경우)
    # 컵라면을 가장 적게준 문제 pop
    if deadline < len(queue):
        heapq.heappop(queue)

print(sum(queue))