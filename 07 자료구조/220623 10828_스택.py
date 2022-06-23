import sys

# 스택 구현
class stack:
    def __init__(self):
        self.s = []
    
    # 푸쉬 함수
    def push(self, num):
        self.s.append(num)
        
    # 팝 함수
    def pop(self):
        # 스택이 비어있는경우 -1 출력
        if len(self.s) == 0:
            print(-1)
        else:
            print(self.s[-1])
            del self.s[-1]

    # 사이즈 함수
    def size(self):
        print(len(self.s))
        
    # empty 함수
    def empty(self):
        if len(self.s) == 0:
            print(1)
        else:
            print(0)
    
    # top 함수
    def top(self):
        if len(self.s) == 0:
            print(-1)
        else:
            print(self.s[-1])
    
# 명령어 횟수 입력
a = int(sys.stdin.readline().rstrip())

# 스택 선언
sta = stack()

# 명령어에 따른 함수호출용 사전
dic = {"pop":sta.pop,
       "size":sta.size,
       "empty":sta.empty,
       "top":sta.top}

for _ in range(a):
    q = sys.stdin.readline().rstrip().split()
    
    # 푸쉬일경우만 q의 길이가 2
    if len(q) == 2:
        sta.push(int(q[1]))
    else:
        dic[q[0]]()