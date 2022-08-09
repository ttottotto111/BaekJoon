import sys
from collections import deque

t = int(sys.stdin.readline().rstrip())
    
def bfs(start, p):
    q = deque()
    q.append(start)
    visited[start] = True
    
    while q:
        # 모두 방문하면
        if visited.count(True) == n:
            return p
        
        curr = q.popleft()
        
        for node in graph[curr]:
            if not visited[node]:
                q.append(node)
                p += 1
                visited[node] = True
            
for _ in range(t):
    n, m = map(int, sys.stdin.readline().rstrip().split())
    
    # 국가 방문상태
    visited = [False]*(n+1)
    
    graph = [[] for _ in range(n+1)]
    
    # 연결되어있는 국가들 추가
    for i in range(m):
        a, b = map(int, sys.stdin.readline().rstrip().split())
        graph[a].append(b)
        graph[b].append(a)
    
    p = bfs(1,0)
    print(p)