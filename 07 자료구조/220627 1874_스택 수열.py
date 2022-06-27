import sys

a = int(sys.stdin.readline().rstrip())

# 수열 저장용 리스트
num_list = []
for _ in range(a):
    num_list.append(int(sys.stdin.readline().rstrip()))
    
# 스택 정보를 저장
num2_list = []
# pop push 정보 저장
pop_push = []

# 스택 숫자 계산용 변수
count = 1

for i in num_list:
    while count <= i:
        num2_list.append(count)
        count += 1
        pop_push.append("+")
    
    # 출력부분이 주어진 수와 같을경우 pop
    if num2_list[-1] == i:
        num2_list.pop()
        pop_push.append("-")
    
    # 출력부분이 다를경우 NO
    else:
        count = "NO"
        break
    
if count == "NO":
    print(count)
else:
    for j in pop_push:
        print(j)