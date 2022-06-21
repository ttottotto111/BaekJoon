import sys

a, b = map(int, sys.stdin.readline().rstrip().split())

# 첫번째 집합
set1 = sys.stdin.readline().rstrip().split()
set1 = [int(i) for i in set1]
set1 = set(set1)

# 두번째 집합
set2 = sys.stdin.readline().rstrip().split()
set2 = [int(i) for i in set2]
set2 = set(set2)

# 각각의 차집합
n1 = set1 - set2
n2 = set2 - set1

# 합집합의 길이 출력
print(len(n1 | n2))