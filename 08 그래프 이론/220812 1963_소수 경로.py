import sys, math
from collections import deque

# 소수 판별을 위해 숫자의 제곱근 내에 있는 수들의 배수를 걸러냄
def findtf():
    # 에라토스테네스의 체
    for i in range(2, 100):
        if tf[i] == True:
            # 소수인 상태에서 소수의 배수 체크
            for j in range(2*i, 10000, i):
                tf[j] = False

# 완전탐색 BFS
def bfs():
    q = deque()
    q.append([a, 0])
    
    # 방문 여부
    # 중복 방지를 위해 큐에 넣은 숫자를 방문 처리
    visited = [0 for i in range(10000)]
    visited[a] = 1
    
    while q:
        now, cnt = q.popleft()
        strnow = str(now)
        
        # 빼낸값이 b면 cnt 반환
        if now == b:
            return cnt

        for i in range(4):
            # 각자리에 0~9를 넣어가며 소수인지 확인
            for j in range(10):
                temp = int(strnow[:i] + str(j) + strnow[i+1:])
                
                # 방문하지 않고, 소수이며, 1000 이상인 숫자인 경우
                if visited[temp] == 0 and tf[temp] and temp >= 1000:
                    visited[temp] = 1
                    q.append([temp, cnt+1])


t = int(sys.stdin.readline().rstrip())

# 소수 판별용 배열
tf = [True for _ in range(10000)]
# 소수 판별
findtf()

for _ in range(t):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    
    # a, b 단계 카운트
    result = bfs()
    
    if result != None:
        print(result)
    else:
        print("Impossible")