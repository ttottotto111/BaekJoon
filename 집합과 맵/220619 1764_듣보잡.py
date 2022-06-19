import sys

a, b = map(int, sys.stdin.readline().rstrip().split(' '))

# 듣지 못한 사람
p1 = set()
for _ in range(a):
    p1.add(sys.stdin.readline().rstrip())

# 듣지 못한 사람중 보지 못한사람만 리스트에 추가
p2 = []
for _ in range(b):
    see = sys.stdin.readline().rstrip()
    if see in p1:
        p2.append(see)

p2.sort()
print(len(p2))
for i in p2:
    print(i)