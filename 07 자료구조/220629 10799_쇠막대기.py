import sys

stick = sys.stdin.readline().rstrip()
# 레이저를 /로 변환
stick = stick.replace("()", "/")

# ( 일경우 막대기로 판단
stick_stack = []
result = 0

for s in stick:
    # ( 일시 스택에 입력
    if s == "(":
        stick_stack.append(s)
    
    
    else:
        # / 일시 레이저라고 판단하여 (의 개수(막대기수)를 결과에 더한다
        if s == "/":
            result += len(stick_stack)
        
        # )) 일시 막대기 끝부분이기 때문에 끝부분을 +1 해준다
        else:
            stick_stack.pop()
            result += 1

print(result)