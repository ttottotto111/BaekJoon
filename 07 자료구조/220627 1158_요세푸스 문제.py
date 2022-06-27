import sys

a, b = map(int, sys.stdin.readline().rstrip().split())

# 앉아있는 사람
person = []
for i in range(1, a+1):
    person.append(i)
    
# 제거할 인덱스 번호
d = 0
# 제거된 번호 리스트
d_num = []

for i in range(a):
    # 앞자리수 1개가 지워지기때문에 b-1
    d += (b-1)
    
    # 만약 d가 남아있는 사람수보다 적다면 나머지값 ==> 한바퀴를 돌았을경우
    if d >= len(person):
        d %= len(person)
    
    d_num.append(person.pop(d))
    
print("<", ', '.join(str(i) for i in d_num), ">", sep = '')