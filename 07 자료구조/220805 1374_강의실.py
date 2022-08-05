import sys
import heapq

n = int(sys.stdin.readline().rstrip())

lecture = []
for _ in range(n):
    lecture.append(list(map(int, sys.stdin.readline().rstrip().split())))

# 끝나는 순서로 정렬, 같다면 시작시간으로 정렬
lecture = sorted(lecture, key=lambda x:(x[1], x[2]))
# 가장먼저 끝나는 강의를 추가
class_room = []
heapq.heappush(class_room, lecture[0][2])

for i in range(1, n):
    # 다음 강의의 시작시간이 현재 진행중인 강의중 가장 먼저 시작한 강의보다 빠를경우
    # 강의실 추가
    if lecture[i][1] < class_room[0]:
        heapq.heappush(class_room, lecture[i][2])
        
    # 강의실이 안겹치는경우
    # 기존강의 제거 후 현재 강의로 변경
    else:
        heapq.heappop(class_room)
        heapq.heappush(class_room, lecture[i][2])

print(len(class_room))