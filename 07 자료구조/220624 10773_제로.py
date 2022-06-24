import sys

a = int(sys.stdin.readline().rstrip())

# 수 기록 리스트
arr = []

for _ in range(a):
    num = int(sys.stdin.readline().rstrip())
    if num != 0:
        arr.append(num)
    else:
        del arr[-1]

print(sum(arr))