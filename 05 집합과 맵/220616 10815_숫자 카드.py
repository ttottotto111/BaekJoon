import sys

# 가지고 있는 카드
# list의 in은 모든 항목을 조회하기때문에 시간이 오래걸려 set사용
card1 = int(sys.stdin.readline().rstrip())
card1_arr = set(sys.stdin.readline().rstrip().split())

# 확인할 카드
card2 = int(sys.stdin.readline().rstrip())
card2_arr = sys.stdin.readline().rstrip().split()

for i in range(card2):
    if card2_arr[i] in card1_arr:
        print(1, end=" ")
    else:
        print(0, end=" ")