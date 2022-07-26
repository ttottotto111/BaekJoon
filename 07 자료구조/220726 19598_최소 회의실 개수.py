import sys
import heapq

n = int(sys.stdin.readline().rstrip())

# 회의 시작, 끝 시간 입력
meeting = []
for _ in range(n):
    meeting.append(list(map(int, sys.stdin.readline().rstrip().split())))

# 끝나는시간 순서대로 정렬, 같다면 시작시간으로 정렬
meeting.sort(key= lambda x: (x[0], x[1]))

# 가장 먼저 끝나는 회의를 큐에 추가
meetingroom = []
heapq.heappush(meetingroom, meeting[0][1])

for m in range(1, n):
    # 다음 회의의 시작시간이 현재 가장 빨리 끝나는 회의보다 빠를경우
    # 회의실 추가
    if meeting[m][0] < meetingroom[0]:
        heapq.heappush(meetingroom, meeting[m][1])
    
    # 다음 회의의 시작시간이 현 가장 빨리 끝나는 회의가 끝나고 진행될경우
    # 회의실 변경
    else:
        heapq.heappop(meetingroom)
        heapq.heappush(meetingroom, meeting[m][1])

# 사용한 강의실 개수 출력
print(len(meetingroom))