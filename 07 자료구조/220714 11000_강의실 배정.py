import sys
import heapq

n = int(sys.stdin.readline().rstrip())

time = []
heap = []

for _ in range(n):
    time.append(list(map(int, sys.stdin.readline().rstrip().split())))

# 끝나는 순서로 정렬, 같다면 시작시간으로 정렬
time = sorted(time, key=lambda x:(x[0], x[1]))
# 가장 먼저 끝나는 강의를 추가
heapq.heappush(heap, time[0][1])

for i in range(1, n):
    # 다음 강의의 시작시간이 현재 진행중인 강의중 가장 먼저 시작한 강의보다 빠를경우
    # 강의실 추가
    if time[i][0] < heap[0]:
        heapq.heappush(heap, time[i][1])
        
    # 강의실이 안겹치는경우
    # 기존강의 제거 후 현재 강의로 변경
    else:
        heapq.heappop(heap)
        heapq.heappush(heap, time[i][1])

print(len(heap))