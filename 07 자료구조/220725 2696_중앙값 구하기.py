import sys
import heapq

t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    m = int(sys.stdin.readline().rstrip())
    
    # 수열
    num_arr = []
    for i in range(m//10 +1):
        num  = list(map(int, sys.stdin.readline().rstrip().split()))
        num_arr += num
    
    # 작은 수, 큰 수를 담을 힙
    small = []
    big = []
    
    # 결과값을 담을 리스트
    result = []
    result_arr = []
    count = 0
    
    for n in num_arr:
        # 두 힙의 크기를 맞춰준다
        if len(small) == len(big):
            heapq.heappush(small, -n)
        else:
            heapq.heappush(big, n)
        
        # 만약 큰수가 작은수힙에 들어왔을경우 큰수의 가장 작은수와 작은수의 가장 큰수를 교환
        # 작은수중 가장 큰수가, 큰 수중 가장 작은수보다 클경우
        if big and -small[0] > big[0]:
            s = heapq.heappop(small)
            b = heapq.heappop(big)
            
            heapq.heappush(small, -b)
            heapq.heappush(big, -s)
        
        # 두 힙의 합/2 가 홀수일경우 (홀수번째 수일경우)
        # 중앙값(작은 수중 가장 큰 값) 출력
        # 10개 입력되었을경우 계행 
        if (len(small)+ len(big)) % 2 == 1:
            result_arr.append(-small[0])
            count += 1
        
        if len(result_arr) == 10:
            result.append(result_arr)
            result_arr = []
    
    # 결과값 출력
    print(count)
    if result:
        for j in result:
            print(*j)
        print(*result_arr)
    else:
        print(*result_arr)