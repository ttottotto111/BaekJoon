import sys

n = int(sys.stdin.readline().rstrip())

# 전체 가입자 리스트
user = []

for i in range(n):
    # 가입자 한사람의 리스트
    one = sys.stdin.readline().rstrip().split(' ')
    one.append(i)
    # 가입순서를 위한 번호
    one[0] = int(one[0])
    
    user.append(one)

# 나이와 가입순서에 따라 정렬
user.sort(key=lambda x:(x[0], x[2]))

for u in range(n):
    print(user[u][0], user[u][1])