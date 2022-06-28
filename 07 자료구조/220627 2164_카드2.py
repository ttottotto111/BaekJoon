import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())

# 카드 리스트
# list의 pop(0)은 뒤의 원소들을 전부 한칸씩 당겨옴
# deque의 popleft는 당겨오는 작업이 없음
card = deque(range(1,n+1))

while len(card) != 1:
    card.popleft()
    card.append(card.popleft())

print(card[0])