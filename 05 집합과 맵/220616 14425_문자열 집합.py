import sys

a,b = map(int, sys.stdin.readline().rstrip().split())

# 주어진 문자열 리스트에 추가
char1 = set()
for _ in range(a):
    char1.add(sys.stdin.readline().rstrip())

# 집합에 포함되있는 문자열
char2 = []
for _ in range(b):
    char2.append(sys.stdin.readline().rstrip())
    
# 총 갯수
count = 0

for i in range(b):
    if char2[i] in char1:
        count += 1

print(count)