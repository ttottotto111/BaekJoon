import sys

# 컴퓨터의 수
n = int(sys.stdin.readline().rstrip())
# 연결할 수 있는 선의 수
m = int(sys.stdin.readline().rstrip())

net = []
root = [i for i in range(n+1)]

for _ in range(m):
    a,b,c = map(int, sys.stdin.readline().rstrip().split())
    net.append([c,a,b])

def findroot(x):
    if root[x] != x:
        root[x] = findroot(root[x])
    return root[x]

# 비용을 기준으로 정렬
result = 0
net.sort()

# 두 컴퓨터의 root를 찾은뒤 같이 않다면
# 비용을 더하고, 더 큰 root값을 작은 root값으로 바꾸어준다
for c, a, b in net:
    fa = findroot(a)
    fb = findroot(b)
    if fa != fb:
        result += c
        if fa < fb:
            root[fb] = fa
        else:
            root[fa] = fb

print(result)