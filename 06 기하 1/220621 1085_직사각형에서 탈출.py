import sys

x,y, w,h = map(int, sys.stdin.readline().rstrip().split())

# x축으로 가는 최소값
if w-x> x:
    x_min = x
else:
    x_min = w-x
    
# y축 최소값
if h-y> y:
    y_min = y
else:
    y_min = h-y

# x와 y 최솝값을 비교후 더 작은값 출력
if x_min > y_min:
    print(y_min)
else:
    print(x_min)