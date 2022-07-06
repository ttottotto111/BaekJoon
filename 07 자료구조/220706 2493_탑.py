import sys

n = int(sys.stdin.readline().rstrip())

top = list(map(int, sys.stdin.readline().rstrip().split()))

# 정답 리스트
result = [0]*n
# 작은값을 넣을 스택 : 초기값은 가장 마지막에 있는 탑
stack = [n-1]

# 마지막에서 두번째에 있는탑에부터 역순으로 반복
for i in range(n-2, -1, -1):
    # 스택에 들어있는 인덱스에 있는 탑이 현재 인덱스의 탑보다 작을경우
    # 정답 리스트에 현재 있는탑의 인덱스 입력 (신호를 받는 탑의 인덱스)
    while len(stack) !=0 and top[stack[-1]]<top[i]:
        result[stack.pop()] = i+1
    stack.append(i)
print(*result)