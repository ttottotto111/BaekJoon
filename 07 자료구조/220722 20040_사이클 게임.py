import sys

n,m = map(int, sys.stdin.readline().rstrip().split())

parent = [i for i in range(n)]

def find(x):
    while x != parent[x]:
        x = parent[x]
    return x

def union(x,y):
    a = find(x)
    b = find(y)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

turn = 0

for i in range(m):
    # 두 점의 번호 입력
    start, end = map(int, sys.stdin.readline().rstrip().split())
    
    # 입력된 끝 점이 시작점과 이어져있다면 턴수 출력
    if find(start) == find(end):
        turn = i+1
        break
    
    # 이어져 있지 않을경우 선 입력
    union(start, end)

print(turn)