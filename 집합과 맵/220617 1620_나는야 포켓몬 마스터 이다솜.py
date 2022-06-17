import sys

a,b = map(int, sys.stdin.readline().rstrip().split())

# 포켓몬 이름이 키
poket_name = dict()
#포켓몬 번호가 키
poket_num = dict()
for i in range(1,a+1):
    poketmon = sys.stdin.readline().rstrip()
    poket_name[poketmon] = i
    poket_num[i] = poketmon


# 결과 출력용 리스트
result = []
for _ in range(b):
    q = sys.stdin.readline().rstrip()
    # 숫자일경우
    if q.isdigit() == True:
        result.append(int(q))     
    # 문자일경우
    else:
        result.append(q)

# 결과 출력
for i in result:
    if type(i) == int:
        print(poket_num[i])
    else:
        print(poket_name[i])