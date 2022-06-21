import sys
from collections import Counter

a = int(sys.stdin.readline())

# 집합에 저장
num = []
for _ in range(a):
    num.append(int(sys.stdin.readline()))
    
# 산술평균 num.mean()도 가능
print(int(round(sum(num)/len(num), 0)))

# 중앙값
num.sort()
print(num[a//2])

# 최빈값
num_arr = Counter(num).most_common()
# 최빈값이 2개이상일 경우
if len(num_arr) > 1 and num_arr[0][1]==num_arr[1][1]:
    print(num_arr[1][0])
# 최빈값이 1개일 경우
else:
    print(num_arr[0][0])
    
# 범위
print(max(num) - min(num))