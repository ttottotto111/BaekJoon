import sys
sys.setrecursionlimit(100000)

def dfs(x,y):
    visited[y][x] = True
    count[-1] += 1
    dfs_x = [-1,1,0,0]
    dfs_y = [0,0,1,-1]
        
    for num in range(4):
        xx = x + dfs_x[num]
        yy = y + dfs_y[num]
        
        if xx >= n or yy >= n or xx < 0 or yy <0:
            continue
        if not visited[yy][xx] and house[yy][xx] == 1:
            dfs(xx,yy)

n = int(sys.stdin.readline().rstrip())

house = []
count = []
visited = [[False]*n for _ in range(n)]
for _ in range(n):
    house.append(list(map(int, sys.stdin.readline().rstrip())))

result = 0
count = []
for y in range(n):
    for x in range(n):
        if not visited[y][x] and house[y][x] == 1:
            count.append(0)
            result += 1
            dfs(x,y)

count.sort()
print(result)
for c in count:
    print(c)