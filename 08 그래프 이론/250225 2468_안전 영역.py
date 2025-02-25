import sys
sys.setrecursionlimit(100000)

def dfs(x,y):
    visited[y][x] = True
    dfs_x = [1,-1,0,0]
    dfs_y = [0,0,1,-1]
    
    for num in range(4):
        xx = x + dfs_x[num]
        yy = y + dfs_y[num]
        
        if xx >= n or yy >= n or xx<0 or yy<0:
            continue
        if not visited[yy][xx] and location[yy][xx] > h:
            dfs(xx,yy)

n = int(sys.stdin.readline().rstrip())

location = []
for _ in range(n):
    location.append(list(map(int, sys.stdin.readline().rstrip().split())))
    
h = 0
result = 0

while True:
    safe = 0
    visited = [[False]*n for _ in range(n)]
    
    for y in range(n):
        for x in range(n):
            if not visited[y][x] and location[y][x] > h:
                dfs(x,y)
                safe += 1
    
    if safe == 0:
        break
    if safe > result:
        result = safe
    
    h += 1
    
print(result)