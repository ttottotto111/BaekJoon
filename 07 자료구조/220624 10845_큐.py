import sys

# 큐의 함수 선언
class queue:
    def __init__(self):
        self.q = []
        
    # PUSH 함수
    def push(self, num):
        self.q.append(num)
        
    # POP 함수
    def pop(self):
        if len(self.q) == 0:
            print(-1)
        else:
            print(self.q[0])
            del self.q[0]
    
    # size 함수
    def size(self):
        print(len(self.q))
    
    # empty 함수
    def empty(self):
        if len(self.q) == 0:
            print(1)
        else:
            print(0)

    # front 함수
    def front(self):
        if len(self.q) == 0:
            print(-1)
        else:
            print(self.q[0])
            
    # back 함수
    def back(self):
        if len(self.q) == 0:
            print(-1)
        else:
            print(self.q[-1])
            
# 명령어 횟수 입력
a = int(sys.stdin.readline().rstrip())

# 큐 선언
que = queue()

# 명령어에 따른 함수호출 사전
q_dic = {"pop": que.pop,
         "size": que.size,
         "empty": que.empty,
         "front": que.front,
         "back": que.back}

# 명령어 실행
for _ in range(a):
    b = sys.stdin.readline().rstrip().split()
    if len(b) > 1:
        que.push(int(b[1]))
    else:
        q_dic[b[0]]()