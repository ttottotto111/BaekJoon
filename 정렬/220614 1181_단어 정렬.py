import sys

n = int(sys.stdin.readline().rstrip())

char = []
for _ in range(n):
    char.append(sys.stdin.readline().rstrip())

# 중복제거를 위해 집합으로 변환
char = set(char)

# 다시 리스트로 변환
char = list(char)

# 상위 조건 A와 하위 조건 B가 있으면 먼저 B로 정렬을 한 후에 A로 정렬
# 문자열 정렬
char.sort()
# 크리순으로 정렬
char.sort(key=len)

for c in char:
    print(c)