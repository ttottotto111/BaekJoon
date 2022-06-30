import sys
from collections import deque

string1 = deque(sys.stdin.readline().rstrip())
string2 = deque()

num = int(sys.stdin.readline().rstrip())

for _ in range(num):
    a = sys.stdin.readline().rstrip().split()
    # 커서 기준 왼쪽의 문자를 string1으로 옮김
    # 커서 기준 오른쪽의 문자를 string2로 옮김
    
    # 커서를 왼쪽으로 옮김 (string1의 가장 오른쪽의 요소가 커서의 오른쪽으로 이동)
    if a[0] == "L":
        if len(string1) != 0:
            string2.appendleft(string1.pop())
    # 커서를 오른쪽으로 옮김 (string2의 가장 왼쪽의 요소가 커서의 왼쪽으로 이동)
    elif a[0] == "D":
        if len(string2) != 0:
            string1.append(string2.popleft())
    # 커서 왼쪽에 있는 문자 삭제 : string1의 가장 오른쪽 요소(커서의 왼쪽 요소) 삭제
    elif a[0] == "B":
        if len(string1) != 0:
            string1.pop()
    # 커서 왼쪽에 문자 추가 : 커서 왼쪽(string1)의 가장 오른쪽에 요소 추가
    else:
        string1.append(a[1])

# 왼쪽과 오른쪽 요소 합침
string = string1 + string2
print("".join(string))