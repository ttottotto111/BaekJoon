import sys

n = int(sys.stdin.readline().rstrip())

num = sys.stdin.readline().rstrip().split()

# 정수형으로 변환
num =  [int(i) for i in num]

# set 형태로 변환하여 중복값 제거
s_num = set(num)
#중복 제거된 리스트
num2 = list(s_num)
num2.sort()

# 압축된 값을 사전에 입력
X = dict()
for i in range(len(num2)):
    X[num2[i]] = i

# 리스트의 좌표를 압축된 좌표 출력
for i in range(n):
    print(X[num[i]], end=' ')