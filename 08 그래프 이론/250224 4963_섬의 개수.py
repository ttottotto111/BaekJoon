import sys
sys.setrecursionlimit(5000)

def dfs(x, y):
    visited[y][x] = True
    dfs_x = [1, 1, 1, -1, -1, -1, 0, 0]
    dfs_y = [-1, 0, 1, -1, 0, 1, -1, 1]
    
    for num in range(8):
        xx = x + dfs_x[num]
        yy = y + dfs_y[num]
    
        if xx >= w or yy >= h or xx<0 or yy<0:
            continue
        if not visited[yy][xx] and m[yy][xx] == 1:
            visited[yy][xx] = True
            dfs(xx, yy)

while True:
    w, h = map(int, sys.stdin.readline().rstrip().split())
    if w == 0 and h == 0:
        break
    
    visited = [[False]*w for _ in range(h)]
    
    m = []
    for _ in range(h):
        m.append(list(map(int, sys.stdin.readline().rstrip().split())))
    
    result = 0
    for y in range(h):
        for x in range(w):
            if not visited[y][x] and m[y][x] == 1:
                dfs(x, y)
                result += 1

    print(result)