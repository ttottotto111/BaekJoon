import sys

n = int(sys.stdin.readline().rstrip())

# 리스트
a = list(map(int, sys.stdin.readline().rstrip().split()))

# 결과값 리스트, 인덱스 저장용 스택
result = [-1]*n
stack = [0]

for i in range(n):
    # 현재 a의 값이 최근 작은수보다 클경우 최근 작은수의 인덱스를 a의 현재값으로 변경
    # 스택에는 가장 밑에 수가 가장 크다.(올라갈수록 작아짐)
    while len(stack)!=0 and a[stack[-1]]<a[i]:
        # 스택에 저장된 값보다 큰 값이 나올경우 그 값보다 작은 값들 모두 pop
        # 결과 리스트의 값을 큰수로 변경
        result[stack.pop()] = a[i]
    stack.append(i)

print(*result)