import sys
from collections import deque

n, m, r = map(int, sys.stdin.readline().rstrip().split())

t = [[] for _ in range(n+1)]
visited = [0]*(n+1)

for _ in range(m):
    u, v = map(int, sys.stdin.readline().rstrip().split())
    
    t[u].append(v)
    t[v].append(u)

# 내림차순으로 조회되어야 하기때문에  reverse
for i in range(1, n+1):
    t[i] = sorted(t[i], reverse=True)

# 이어지는 정점리스트를 저장할 큐
q = deque()
q.append(r)
count = 1

while q:
    s = q.popleft()
    if visited[s]:
        continue
    
    visited[s] = count
    q.extend(t[s])
    count += 1

for i in range(1, n+1):
    print(visited[i])