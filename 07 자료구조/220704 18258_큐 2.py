import sys
from collections import deque

class que:
    def __init__(self) :
        self.q = deque()
    
    # push
    def push(self, num):
        self.q.append(num)
    
    # pop
    def pop(self):
        if len(self.q) == 0:
            print(-1)
        else:
            print(self.q.popleft())
    
    # size
    def size(self):
        print(len(self.q))
    
    # empty
    def empty(self):
        if len(self.q)==0:
            print(1)
        else:
            print(0)
    
    # front
    def front(self):
        if len(self.q)==0:
            print(-1)
        else:
            print(self.q[0])
    
    # back
    def back(self):
        if len(self.q)==0:
            print(-1)
        else:
            print(self.q[-1])

n = int(sys.stdin.readline().rstrip())

# 큐
q = que()
# 함수 실행용 사전
q_dict = {
    "push" : q.push,
    "pop" : q.pop,
    "size" : q.size,
    "empty" : q.empty,
    "front" : q.front,
    "back" : q.back
}

for _ in range(n):
    cm = sys.stdin.readline().rstrip().split()
    
    # push일 경우
    if len(cm) > 1:
        q_dict[cm[0]](cm[1])
    
    # 나머지 함수
    else:
        q_dict[cm[0]]()