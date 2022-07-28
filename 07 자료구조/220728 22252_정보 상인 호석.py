import sys
import heapq

q = int(sys.stdin.readline().rstrip())\

# 정보 고릴라 정보 사전
information = dict()

# 결과값
result = 0

for _ in range(q):
    query = sys.stdin.readline().rstrip().split()  
    
    # 1일경우 : 사전에 정보 고릴라별 정보 추가
    # 가장 비싼 정보부터 구매하기 때문에 최대값 힙 생성
    if query[0] == "1":
        info = query[-int(query[2]):]
        info = [-int(i) for i in info]
        heapq.heapify(info)
        
        if query[1] in information:
            for i in info:
                heapq.heappush(information[query[1]], i)
        else:
            information[query[1]] = info
    
    # 2일 경우 : 
    else:
        # 원하는 정보 고릴라가 있을경우
        if query[1] in information:
            # 정보고릴라의 정보수가 원하는 정보수보다 적을경우 (모두구매)
            if len(information[query[1]]) < int(query[2]):
                for i in range(len(information[query[1]])):
                    result += heapq.heappop(information[query[1]])
                    
            # 정보수가 원하는 것보다 많을경우
            # 원하는 정보 수만큼 큰 정보부터 구매
            else:
                for i in range(int(query[2])):
                    result += heapq.heappop(information[query[1]])

print(-result)