import sys
from collections import deque

s = sys.stdin.readline().rstrip()

# 괄호 체크
string = ""
result = deque()

for s1 in s:
    # 괄호 열림
    if s1 == "<":
        string = s1
        result.append(s1)
        continue
    # 괄호 닫힘 : 출력 후 큐 초기화
    if s1 == ">":
        string = s1
        result.append(s1)
        print("".join(result), end="")
        result = deque()
        continue
    # 띄어쓰기일경우
    if s1 == " ":
        # 괄호가 열려있지 않으면 출력 후 큐 초기화
        if string == ">" or string == "":
            print("".join(result), end=" ")
            result = deque()
            continue
        # 괄호가 열려있을경우 큐에 입력
        else:
            result.append(s1)
            continue
    
    # 특수문자가 아닐경우
    # 괄호가 열려있는 상태가 아닐경우 : 큐의 앞에 문자 추가
    if string == "" or string == ">":
        result.appendleft(s1)
    else:
        result.append(s1)

print("".join(result))