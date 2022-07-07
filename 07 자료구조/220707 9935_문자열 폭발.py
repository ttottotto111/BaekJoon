import sys

string = sys.stdin.readline().rstrip()
bomb = list(sys.stdin.readline().rstrip())

# 문자열 추가후, 스택 맨 뒤 문자가 폭탄문자열과 같을경우 제거
stack = []

if len(bomb) == 1:
    for i in string:
        if i==bomb[0]:
            continue
        stack.append(i)
else:
    for i in string:
        stack.append(i)
        if stack[-1]==bomb[-1] and stack[-len(bomb):] == bomb:
            for _ in range(len(bomb)):
                stack.pop()

if stack:
    print("".join(stack))
else:
    print("FRULA")