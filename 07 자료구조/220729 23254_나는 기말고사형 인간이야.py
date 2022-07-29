import sys
import heapq

n, m = map(int, sys.stdin.readline().rstrip().split())

# 기존 점수
before = list(map(int, sys.stdin.readline().rstrip().split()))
# 공부했을시 오르는 수치
study = list(map(int, sys.stdin.readline().rstrip().split()))

# 점수 변환관리용 힙
after = []
# 100점인 점수 카운트
score_100 = 0

# 오르는 점수를 기준으로 최대힙 생성
for i in range(m):
    heapq.heappush(after, [-study[i], before[i]])

n *= 24

# 공부시간만큼 반복
# 점수가 가장 많이 오르는 과목부터 점수 증가
while after[0][0] != 0 and n != 0:
    a, c = heapq.heappop(after)
    # 가장 높은 점수가 오르는 과목을 우선적으로 최대한 공부
    s = (100-c)//-a
    
    # 정해진 시간보다 공부시간이 적을경우
    if n>= s:
        n -= s
    # 공부하는 시간이 정해진 시간을 초과한경우
    else:
        s = n
        n = 0
        
    after_score = s * -a + c
    heapq.heappush(after, [after_score-100, after_score])
    
result = 0
for j, k in after:
    result += k
    
print(result)