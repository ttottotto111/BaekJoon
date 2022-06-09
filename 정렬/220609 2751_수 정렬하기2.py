import sys

a = int(input())

# 집합에 저장
num = []
for _ in range(a):
    num.append(int(sys.stdin.readline()))

#정렬
num.sort()

for n in num:
    print(n)