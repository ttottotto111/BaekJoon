import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())

for _ in range(n):
    # 커서 왼쪽 오른쪽 큐
    left = deque()
    right = deque()
    string = sys.stdin.readline().rstrip()
    
    for s in string:
        if s in "<>-":
            # 커서 왼쪽이동
            if s == "<" and left:
                right.appendleft(left.pop())
            # 커서 오른쪽 이동
            if s == ">" and right:
                left.append(right.popleft())
            # 삭제
            if s == "-" and left:
                left.pop()
        else:
            left.append(s)
    
    result = left + right
    print("".join(result))