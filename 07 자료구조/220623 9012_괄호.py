import sys

a = int(sys.stdin.readline().rstrip())

for i in range(a):
    s = sys.stdin.readline().rstrip()
    count = 0
    
    # (일경우 +1  )일경우 -1
    # count가 -1 경우 => 열려있는 괄호보다 닫혀있는 괄호가 더 많다
    # count가 0보다 클경우 => 열려있는 괄호보다 닫혀있는 괄호가 더 적다
    for ss in s:
        if count == -1:
            break
        
        if ss =="(":
            count += 1
        else:
            count -= 1
        
    if count == 0:
        print("YES")
    else:
        print("NO")