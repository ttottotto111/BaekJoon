import sys
sys.setrecursionlimit(100000)

def dfs(x,y,c):
    if c == 0:
        visited_n[y][x] = True
    else:
        visited_c[y][x] = True
    dfs_x = [-1,1,0,0]
    dfs_y = [0,0,-1,1]
    
    for num in range(4):
        xx = x + dfs_x[num]
        yy = y + dfs_y[num]
        if xx >= n or yy >= n or xx < 0 or yy < 0:
            continue
        if c == 0 and not visited_n[yy][xx]:
            if picture[y][x] == picture[yy][xx]:
                dfs(xx,yy,0)
        if  c == 1 and not visited_c[yy][xx]:
            if picture[y][x] == 'R' or picture[y][x] == 'G':
                if picture[yy][xx] == 'R' or picture[yy][xx] == 'G':
                    dfs(xx,yy,1)
            else:
                if picture[yy][xx] == 'B':
                    dfs(xx,yy,1)
            

n = int(sys.stdin.readline().rstrip())

picture = []
visited_n = [[False]*n for _ in range(n)]
visited_c = [[False]*n for _ in range(n)]
for _ in range(n):
    picture.append(list(sys.stdin.readline().rstrip()))

result = [0,0]
for y in range(n):
    for x in range(n):
        if not visited_n[y][x]:
            result[0] += 1
            dfs(x,y,0)
        if not visited_c[y][x]:
            result[1] += 1
            dfs(x,y,1)

print(f"{result[0]} {result[1]}")