import sys

while True:
    a = sys.stdin.readline().rstrip()
    if a == ".":
        break
    
    # 괄호 저장용 스택
    braket = []
    
    for s in a:
        # 열린괄호일경우 스택에 저장
        if s == "(" or s == "[":
            braket.append(s)
        
        # 소괄호 닫을경우 (마지막에 넣은게 소괄호일때 대괄호가 닫히면 no)
        elif s == ")":
            if len(braket) > 0 and braket[-1] == "(":
                braket.pop()
            else:
                braket.append(s)
                break
        
        # 대괄호 닫을경우
        elif s == "]":
            if len(braket) > 0 and braket[-1] == "[":
                braket.pop()
            else:
                braket.append(s)
                break
    
    # 스택 안에 괄호가 남아있을경우 no
    if len(braket) == 0:
        print("yes")
    else:
        print("no")