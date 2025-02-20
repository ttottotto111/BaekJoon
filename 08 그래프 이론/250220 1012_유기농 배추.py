import sys
sys.setrecursionlimit(100000)

def dfs(x, y):
    visited[y][x] = True
    dfs_x = [1,-1,0,0]
    dfs_y = [0,0,1,-1]
    
    for num in range(4):
        xx = x + dfs_x[num]
        yy = y + dfs_y[num]

        if xx >= len(visited[0]) or yy >= len(visited) or xx<0 or yy<0:
            continue
        if not visited[yy][xx] and g[yy][xx] == 1:
            dfs(xx,yy)

t = int(sys.stdin.readline().rstrip())

for __ in range(t):
    m,n,k  = map(int, sys.stdin.readline().rstrip().split())
    
    # 그래프 생성
    g = [[0]*m for _ in range(n)]
    visited = [[False]*m for _ in range(n)]

    # 배추 위치
    for _ in range(k):
        x,y = map(int, sys.stdin.readline().rstrip().split())
        g[y][x] = 1

    result = 0
    for y in range(n):
        for x in range(m):
            if not visited[y][x] and g[y][x] == 1:
                dfs(x,y)
                result += 1

    print(result)