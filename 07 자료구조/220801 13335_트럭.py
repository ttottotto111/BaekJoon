import sys

n, w, l = map(int, sys.stdin.readline().rstrip().split())
truck = list(map(int, sys.stdin.readline().rstrip().split()))

bridge = [0] * w
result = 0

while bridge:
    result += 1
    # 다리의 칸을 하나씩 줄인다.
    bridge.pop(0)
    
    if truck:
        # 현재 다리에 있는 트럭과 건너려는 트럭의 무게가
        # 다리의 하중보다 크다면 빈공간 추가
        if sum(bridge) + truck[0] >l:
            bridge.append(0)
        else:
            bridge.append(truck.pop(0))

print(result)