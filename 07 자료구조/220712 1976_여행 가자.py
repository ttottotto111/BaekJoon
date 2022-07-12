import sys

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, x,y):
    a = find(parent, x)
    b = find(parent, y)
    if a>b:
        parent[a] = b
    else:
        parent[b] = a
    

n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())

# 이어진 도시 정보를 부모값으로 저장용 리스트
parent = [i for i in range(n+1)]

# 주어진 도시 정보
route = []
for _ in range(n):
    route.append(list(map(int, sys.stdin.readline().rstrip().split())))

# 여행 계획
plan = list(map(int, sys.stdin.readline().rstrip().split()))

# 이어진 도시정보를 부모값으로 초기화
for i in range(n):
    for j in range(i+1, n):
        if route[i][j] == 1:
            union(parent, i+1, j+1)

# 여행 시작 도시를 지정
firstplan = find(parent, plan[0])

# 여행 계획만큼 반복 시작도시와 이어져 있지 않는경우 fail
for a in range(m):
    if find(parent, plan[a]) != firstplan:
        print("NO")
        exit()
print("YES")