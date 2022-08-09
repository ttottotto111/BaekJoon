import sys

# DFS 방식

n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())

computer = {}

# 연결된 컴퓨터 표시용 사전에 컴퓨터 등록
for i in range(n):
    computer[i+1] = set()
    
for j in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    computer[a].add(b)
    computer[b].add(a)

# 1번 컴퓨터와 연결된 컴퓨터들을 재귀를 사용해 카운트
def dfs(s, computer):
    for i in computer[s]:
        if i not in visited:
            visited.append(i)
            dfs(i, computer)

visited = []
dfs(1, computer)
# 본인을 제외한 나머지 개수 출력
print(len(visited)-1)