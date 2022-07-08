import sys

n = sys.stdin.readline().rstrip()

breaker = False
stack = []

for i in n:
    # ( , [
    if i =="(" or i =="[":
        stack.append(i)
    
    # )
    elif i == ")" and stack:
        if stack[-1] == "(":
            stack[-1] = 2
        
        else:
            temp = 0
            for _ in range(len(stack)):
                # 괄호가 닫힐경우 더하던 숫자에 2를 곱함
                if stack[-1] == "(":
                    stack[-1] = temp * 2
                    break
                # ) 인데 [ 로 시작했을경우
                elif stack[-1] == "[":
                    breaker = True
                    break
                # 숫자일경우 더하기
                else:
                    temp += stack[-1]
                    stack.pop()
    
    # ]
    elif i=="]" and stack:
        if stack[-1] == "[":
            stack[-1] =3
        
        else:
            temp = 0
            for _ in range(len(stack)):
                # 괄호가 닫힐경우 더한 숫자에 3을 곱해준다
                if stack[-1] == "[":
                    stack[-1] = temp * 3
                    break
                # ] 인데 ( 로 시작했을경우
                elif stack[-1] == "(":
                    breaker = True
                    break
                # 숫자일경우 더하기
                else:
                    temp += stack[-1]
                    stack.pop()
                    
    # 괄호가 열리지않고 닫힌 괄호만 있을경우
    else:
        breaker = True
        break

# 괄호가 남아있을 경우에도 실패
if breaker or "(" in stack or "["in stack:
    print(0)
else:
    print(sum(stack))