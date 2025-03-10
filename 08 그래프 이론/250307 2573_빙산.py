import sys
import copy
sys.setrecursionlimit(100000)

def dfs(x,y):
    visited[y][x] = True
    dfs_x = [1,-1,0,0]
    dfs_y = [0,0,1,-1]
        
    for num in range(4):
        xx = x + dfs_x[num]
        yy = y + dfs_y[num]
        
        if xx >= m or yy >= n or xx < 0 or yy <0:
            continue
        if not visited[yy][xx] and sea[yy][xx] > 0:
            dfs(xx,yy)

def ice_chk(x,y):
    dfs_x = [-1,1,0,0]
    dfs_y = [0,0,-1,1]
    count = 0
    for num in range(4):
        xx = x + dfs_x[num]
        yy = y + dfs_y[num]
        
        if xx >= m or yy >= n or xx < 0 or yy < 0:
            continue
        if sea[yy][xx] <= 0:
            count += 1
    return count

n,m = map(int, sys.stdin.readline().rstrip().split())

sea = []
ice = []
for _ in range(n):
    sea.append(list(map(int, sys.stdin.readline().rstrip().split())))
after_sea = copy.deepcopy(sea)
    
for y in range(n):
    for x in range(m):
        if sea[y][x] > 0:
            ice.append([y,x])

year = 0
while True:
    if len(ice) == 0:
        print(0)
        break
    visited = [[False]*m for _ in range(n)]
    ice_count = 0
    
    # 빙산 덩어리
    for y, x in ice:
        if not visited[y][x] and sea[y][x] > 0:
            dfs(x,y)
            ice_count += 1
    if ice_count >= 2:
        print(year)
        break
    
    # 1년 뒤 빙산
    temp = []
    for ice_n in range(len(ice)):
        ice_y = ice[ice_n][0]
        ice_x = ice[ice_n][1]
        
        after_sea[ice_y][ice_x] -= ice_chk(ice_x,ice_y)
        if after_sea[ice_y][ice_x] >0:
            temp.append([ice_y, ice_x])
        else:
            after_sea[ice_y][ice_x] = 0
            
    ice = copy.deepcopy(temp)
    sea = copy.deepcopy(after_sea)
    year += 1