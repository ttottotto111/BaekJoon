import sys

n = int(sys.stdin.readline().rstrip())

building = [int(sys.stdin.readline().rstrip()) for i in range(n)]
stack = []
result = 0

for i in range(n):
    # 최근에 넣은 빌딩이 현재 비교할 빌딩보다 크기가 작을경우
    # stack에서 제거 : 현재 건물의 옥상을 볼 수 없기 때문
    while stack and stack[-1] <= building[i]:
        stack.pop()
    
    # 현재 건물을 볼 수 있는 다른 건물들의 개수를 입력
    stack.append(building[i])
    # -1 : 자기 자신은 제거
    result += len(stack) -1

print(result)