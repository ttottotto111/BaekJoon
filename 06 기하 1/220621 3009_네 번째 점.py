import sys

# 리스트에 저장
rec = []
for _ in range(3):
    x,y = map(int, sys.stdin.readline().rstrip().split())
    rec.append([x,y])

# x축끼리 y축끼리 분리
point = [[rec[0][0],rec[1][0],rec[2][0]],[rec[0][1],rec[1][1],rec[2][1]]]

# 카운트를 위해 x축, y축의 중복값 제거
x = set(point[0])
x = list(x)
y = set(point[1])
y = list(y)

# x축중 1개인 좌표
if point[0].count(x[0]) == 2:
    print(x[1], end=' ')
else:
    print(x[0], end=' ')

# y축중 1개인 좌표
if point[1].count(y[0]) == 2:
    print(y[1], end=' ')
else:
    print(y[0], end=' ')