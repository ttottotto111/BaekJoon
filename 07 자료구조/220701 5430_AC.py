import sys
from collections import deque

t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    # 수행할 함수
    p = deque(sys.stdin.readline().rstrip())
    # 수의 개수
    n = int(sys.stdin.readline().rstrip())
    # 배열
    x = sys.stdin.readline().rstrip()
    if n>0:     
        x = deque(x[1:-1].split(","))
    else:
        x = []
        
    # 뒤집은 상태 False : 정상
    reverse = False
    # 에러일경우
    breaker = False

    for a in range(len(p)):
        if p[0] == "R":
            if reverse == False:
                reverse = True
            else:
                reverse = False
            p.popleft()
        else:
            if len(x) == 0:
                breaker = True
                break
            if reverse == False:
                x.popleft()
                p.popleft()
            else:
                x.pop()
                p.popleft()
                
    if reverse == True:
        x.reverse()                 
    if breaker == False:
        print("[", end="")
        print(",".join(x), end="")
        print("]")
    else:
        print("error")