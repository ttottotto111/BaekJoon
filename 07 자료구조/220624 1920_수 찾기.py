import sys

a = int(sys.stdin.readline().rstrip())

# 주어진 수 set이 찾는 속도가 빠르기 때문에 set사용
num_arr1 = sys.stdin.readline().rstrip().split()
num_arr1 = set(num_arr1)

# 비교할 문자열
b = int(sys.stdin.readline().rstrip())
num_arr2 = sys.stdin.readline().rstrip().split()

for i in num_arr2:
    if i in num_arr1:
        print(1)
    else:
        print(0)