import sys

n = int(sys.stdin.readline().rstrip())

xy = []
# 리스트에 좌표를 2차원배열 형태로 저장
for _ in range(n):
    xy_arr = sys.stdin.readline().rstrip().split(' ')
    xy_arr = [int(i) for i in xy_arr]
    xy.append(xy_arr)

# 람다를 사용해 첫번째값을 기준으로 정렬, 같을경우 2번째값으로 정렬
xy.sort(key=lambda x:(x[0], x[1]))

for s in xy:
    print(s[0], s[1])