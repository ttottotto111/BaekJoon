import sys
from collections import deque

# 보드크기
board = int(sys.stdin.readline().rstrip())
# 사과의 개수
apple = int(sys.stdin.readline().rstrip())

# 사과의 좌표
apple_arr = []
for _  in range(apple):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    apple_arr.append([x,y])

# 방향전환 횟수
change_num = int(sys.stdin.readline().rstrip())
# 방향전환 시간, 방향 리스트
change_time = []
change_way = deque()
# 방향 전환 정보
for _ in range(change_num):
    t, w = map(str, sys.stdin.readline().rstrip().split())
    change_time.append(int(t))
    change_way.append(w)
    
# 뱀의 몸통들의 좌표를 담을 큐
snake = deque()
snake.append([1,1])
snakehead = [1,1]
# 뱀이 보고있는 방향
see = "right"

# 경과시간 카운트
result = 0

#게임 시작
while True:   
    # 앞으로 이동
    result += 1 

    # 머리좌표 1칸 이동
    if see == "right":
        snakehead = [snakehead[0], snakehead[1]+1]
    elif see== "down":
        snakehead = [snakehead[0]+1, snakehead[1]]
    elif see== "left":
        snakehead = [snakehead[0], snakehead[1]-1]
    else:
        snakehead = [snakehead[0]-1, snakehead[1]]
        
    # 머리가 몸, 벽에 닿았을 경우
    if (snakehead in snake) or (snakehead[0]*snakehead[1])<=0 or snakehead[0]>board or snakehead[1] > board:
        break 
    else:
        snake.append(snakehead)
        snake.popleft()
        
    # 사과를 먹었을 경우
    if snakehead in apple_arr:
        snake.appendleft(snake[0])
        apple_arr.remove(snakehead)

    # 해당 시간이 지났을 경우 방향 전환
    if result in change_time:
        if change_way[0] == "D":
            if see == "right":
                see = "down"
            elif see == "down":
                see = "left"
            elif see == "left":
                see = "up"
            else:
                see = "right"
            change_way.popleft()
        else:
            if see == "right":
                see = "up"
            elif see == "up":
                see = "left"
            elif see == "left":
                see = "down"
            else:
                see = "right"
            change_way.popleft()

print(result)