import sys

t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    n = int(sys.stdin.readline().rstrip())
    
    # 전화번호 받기
    p_num = []
    for i in range(n):
        p_num.append(sys.stdin.readline().rstrip())
    
    # 받은전화번호를 정렬
    p_num.sort()

    for index in range(n-1):
        length = len(p_num[index])
        if p_num[index] == p_num[index+1][:length]:
            print("NO")
            break
    else:
        print("YES")