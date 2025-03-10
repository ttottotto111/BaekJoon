import sys
sys.setrecursionlimit(100000)

def dfs(x,y):
    visited[y][x] = True
    extent[-1] += 1
    dfs_x = [1,-1,0,0]
    dfs_y = [0,0,1,-1]
    
    for num in range(4):
        xx = x + dfs_x[num]
        yy = y + dfs_y[num]
        
        if xx >= n or yy >= m or xx<0 or yy<0:
            continue
        if not visited[yy][xx] and paper[yy][xx] == 0:
            dfs(xx,yy)

m,n,k = map(int, sys.stdin.readline().rstrip().split())

paper = [[0]*n for _ in range(m)]
visited = [[False]*n for _ in range(m)]

for _ in range(k):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().rstrip().split())
    for i in range(y2, y1, -1):
        for j in range(x1, x2):
            paper[m-i][j] = 1

result = 0
extent = []
for y in range(m):
    for x in range(n):
        if not visited[y][x] and paper[y][x] == 0:
            result += 1
            extent.append(0)
            dfs(x,y)
extent.sort()            

print(result)
print(*extent)