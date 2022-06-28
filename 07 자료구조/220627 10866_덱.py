import sys
from collections import deque

class Deque():
    def __init__(self):
        self.dq = deque()
    
    # push front : 앞에 정수 x 추가
    def push_front(self, x):
        self.dq.appendleft(x)
    
    # push back : 뒤에 정수 x 추가
    def push_back(self, x):
        self.dq.append(x)
        
    # pop front : 앞에 정수 제거, 없는경우 -1 출력
    def pop_front(self):
        if len(self.dq) == 0:
            print(-1)
        else:
            print(self.dq.popleft())
    
    # pop left: 뒤에 정수제거, 없는경우 -1 출력
    def pop_back(self):
        if len(self.dq) == 0:
            print(-1)
        else:
            print(self.dq.pop())
            
    # size : 덱에 들어있는 정수의 개수
    def size(self):
        print(len(self.dq))
    
    # empty : 비어있으면 1, 아니면 0 출력
    def empty(self):
        if len(self.dq) == 0:
            print(1)
        else:
            print(0)
    
    # front : 맨앞에 있는 정수 출력, 없을경우 -1출력
    def front(self):
        if len(self.dq) == 0:
            print(-1)
        else:
            print(self.dq[0])
            
    # back : 맨뒤의 정수 출력, 없을경우 -1 출력
    def back(self):
        if len(self.dq) == 0:
            print(-1)
        else:
            print(self.dq[-1])
            
# 명령 횟수
a = int(sys.stdin.readline().rstrip())

d = Deque()

# 명령어 사전
q = {
    "push_front" : d.push_front,
    "push_back" : d.push_back,
    "pop_front" : d.pop_front,
    "pop_back" : d.pop_back,
    "size" : d.size,
    "empty" : d.empty,
    "front" : d.front,
    "back" : d.back
}

# 명령어 실행
for _ in range(a):
    p = sys.stdin.readline().rstrip().split()
    
    # push 일경우
    if len(p) > 1:
        q[p[0]](p[1])
    
    else:
        q[p[0]]()