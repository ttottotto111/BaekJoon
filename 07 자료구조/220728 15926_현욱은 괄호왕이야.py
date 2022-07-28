import sys

n = int(sys.stdin.readline().rstrip())

bracket = sys.stdin.readline().rstrip()

# 정상적인 괄호 카운트를 위한 리스트
count = [0 for _ in range(n)]
# 괄호 판단용 스택
stack = []

for i in range(n):
    # 여는괄호일 경우 스택에 저장
    if bracket[i] == "(":
        stack.append(i)
    
    # 닫는 괄호일 경우 
    else:
        # 만약 스택에 이미 값이 있다면 짝이 맞는 괄호 (여는 괄호가 이미 있고 이후에 닫히기 때문)
        if stack:
            # 닫는 괄호의 인덱스와, 짝을 이룬 여는괄호의 인덱스를 1로 변경
            count[i] = 1
            count[stack[-1]] = 1
            stack.pop()

# 연속된 1이 가장 많은 부분을 찾는다
result = 0
max_result = 0
for c in count:
    if c == 1:
        result += 1
        max_result = max(max_result, result)
    else:
        result = 0

print(max_result)