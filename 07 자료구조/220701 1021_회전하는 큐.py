import sys
from collections import deque

n,m = map(int, sys.stdin.readline().rstrip().split())

# 큐 생성, 뽑아낼 수
n = deque(i for i in range(1, n+1))
num = sys.stdin.readline().rstrip().split()
num = deque(int(i) for i in num)

# 연산 횟수
count = 0

for _ in range(m):
    i = num[0]
    # n에서 뽑아낼수의 자리가 중간보다 크거나 같을경우 : 오른쪽에서 연산수행
    if n.index(i) >= len(n)/2:
        # 뽑아낼 수가 맨앞자리까지 올때까지 오른쪽으로 이동
        while True:
            if n[0] == num[0]:
                n.popleft()
                num.popleft()
                break
            n.appendleft(n.pop())
            count += 1
    
    # n에서 뽑아낼수의 자리가 중간보다 작을경우 : 왼쪽에서 연산
    else:
        # 뽑아낼 수가 맨앞자리까지 올때까지 왼쪽으로 이동
        while True:
            if n[0] == num[0]:
                n.popleft()
                num.popleft()
                break
            n.append(n.popleft())
            count += 1

print(count)