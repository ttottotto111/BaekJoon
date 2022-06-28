import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())

for _ in range(n):
    # 문서의 개수 a, 궁금한 문서 b
    a,b = map(int, sys.stdin.readline().rstrip().split())
    
    # 문서 중요도 리스트
    doc = deque(map(int, sys.stdin.readline().rstrip().split()))
    # 문서 번호 리스트
    doc_num = deque([number for number in range(a)])
    
    # 출력 횟수
    count = 0
    while True:
        # 첫번째 값이 가장 큰값이면 +1
        if doc[0] == max(doc):
            count += 1
            
            # 가장 큰값이 지정된 문서일 경우
            if doc_num[0] == b:
                print(count)
                break            
            # 아닐경우 맨 앞의 값(가장 큰 값) 삭제
            else:
                doc.popleft()
                doc_num.popleft()
        
        # 첫번째 값이 가장 큰 값이 아니면
        else:
            doc.append(doc.popleft())
            doc_num.append(doc_num.popleft())