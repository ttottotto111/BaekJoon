import sys

# 가지고 있는 카드들
a = int(sys.stdin.readline().rstrip())
card = sys.stdin.readline().rstrip().split(' ')

# 카드들의 갯수를 사전에 저장
count = dict()
for i in card:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1

# 구해야할 카드갯수
b =  int(sys.stdin.readline().rstrip())
card2 = sys.stdin.readline().rstrip().split(' ')

for j in card2:
    if j in count:
        print(count[j], end=' ')
    else:
        print(0, end=' ')