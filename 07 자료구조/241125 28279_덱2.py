import sys
from collections import deque

t = int(sys.stdin.readline().rstrip())
deck = deque()

for _ in range(t):
    input = list(map(int, sys.stdin.readline().rstrip().split()))
    order = input[0]
    
    if order == 1:
        deck.appendleft(input[1])
    elif order == 2:
        deck.append(input[1])
    elif order == 3:
        if deck:
            print(deck.popleft())
        else:
            print(-1)
    elif order == 4:
        if deck:
            print(deck.pop())
        else:
            print(-1)
    elif order == 5:
        print(len(deck))
    elif order == 6:
        if deck:
            print(0)
        else:
            print(1)
    elif order == 7:
        if deck:
            print(deck[0])
        else:
            print(-1)
    elif order == 8:
        if deck:
            print(deck[-1])
        else:
            print(-1)