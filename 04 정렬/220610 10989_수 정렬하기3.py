import sys

a = int(sys.stdin.readline())

# 집합에 저장
num = [0] * 10001

# 리스트의 입력된 수 인덱스에 접근하여 +1을 해줌. 한 번 입력되었다는 뜻
for _ in range(a):
    num[int(sys.stdin.readline())] += 1

for n in range(1,10001):
    # 1~10000의 인덱스 값중 0이 아닌값(입력된 값)
    if num[n] !=0:
        # 입력된 수만큼 해당 숫자 출력 (4가 2번인경우 4 2번출력)
        for _ in range(num[n]):
            print(n)