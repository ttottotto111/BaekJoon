import sys
from collections import deque

n, m  = map(int, sys.stdin.readline().rstrip().split())

# 미로 생성
maze = []
for _ in range(n):
    maze.append(list(map(int, sys.stdin.readline().rstrip())))

# 방향 설정(상하좌우)
dx = [-1,1,0,0]
dy = [0,0,-1,1]

queue = deque()
queue.append([0,0])

while queue:
    x,y = queue.popleft()
    
    for i in range(4):
        move_x = x + dx[i]
        move_y = y + dy[i]
        
        # 미로를 벗어난 경우
        if move_x < 0 or move_x >= n or move_y < 0 or move_y >= m:
            continue
        
        # 갈수 없는 곳일경우
        if maze[move_x][move_y] == 0:
            continue
        
        if maze[move_x][move_y] == 1:
            maze[move_x][move_y] = maze[x][y] + 1
            queue.append([move_x, move_y])

print(maze[n-1][m-1])