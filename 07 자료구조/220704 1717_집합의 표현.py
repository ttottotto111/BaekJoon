# union find 알고리즘
import sys
sys.setrecursionlimit(10**6)

# 집합의 수, 연산 수 입력
n,m = map(int, sys.stdin.readline().rstrip().split())
# 부모 테이블 초기화
parent = [i for i in range(n+1)]

# 특정 원소가 포함된 집합
def find(x):
    # 루트 노드를 찾을때까지 반복
    if parent[x] != x:
        parent[x] =  find(parent[x])
        
    return parent[x]

# 두 원소가 포함된 집합 합치기
def union(a,b):
    a = find(a)
    b = find(b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b

# 연산 실행
for _ in range(m):
    cm = list(map(int, sys.stdin.readline().rstrip().split()))
    
    # 합집합 (유니온 연산)
    if cm[0] == 0:
        union(cm[1], cm[2])
        
    # 두 숫자가 속한 집합 출력 (find연산)
    else:
        if find(cm[1]) == find(cm[2]):
            print("YES")
        else:
            print("NO")