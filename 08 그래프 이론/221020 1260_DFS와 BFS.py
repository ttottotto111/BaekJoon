import sys
from collections import deque

n, m, v = map(int, sys.stdin.readline().rstrip().split())
graph = dict()
dfs_visited = [False] * (n+1)
bfs_visited = dfs_visited.copy()
stack = []

for _ in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())

    if a not in graph:
        graph[a] = [b]
    else:
        graph[a].append(b)
    if b not in graph:
        graph[b] = [a]
    else:
        graph[b].append(a)
        
for i in graph:
    graph[i].sort()


# 넓이우선 탐색 : 큐
def bfs(num):
    queue = deque([num])
    bfs_visited[num] = True
    while queue:
        n = queue.popleft()
        print(n, end=" ")
        if num in graph:
            for i in graph[n]:
                if not bfs_visited[i]:
                    queue.append(i)
                    bfs_visited[i] = True

# 깊이우선 탐색 : 스택
def dfs(num):
    dfs_visited[num] = True
    print(num, end=" ")
    
    if num in graph:
        for i in graph[num]:
            if not dfs_visited[i]:
                dfs(i)

dfs(v)
print()
bfs(v)