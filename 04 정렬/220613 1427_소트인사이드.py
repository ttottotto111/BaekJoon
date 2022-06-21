import sys

n = list(sys.stdin.readline().rstrip())

# 리스트안의 숫자를 int형으로 변환
n = [int(i) for i in n]

# 리스트 정렬
n.sort(reverse=True)

for i in n:
    print(i, end='')