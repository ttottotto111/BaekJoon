import sys

test = int(sys.stdin.readline().rstrip())

for _ in range(test):
    wear_num = int(sys.stdin.readline().rstrip())
    
    # 의상 저장용 사전
    wear_dict = dict()
    
    # 의상을 사전에 등록
    for i in range(wear_num):
        wear = sys.stdin.readline().rstrip().split()      
        # 사전에 이미 등록되어있을경우
        if wear[1] in wear_dict:
            wear_dict[wear[1]].append(wear[0])
        # 사전에 등록이 안되어있을경우
        else:
            wear_dict[wear[1]] = [wear[0]]
    
    # 경우의 수
    # 경우의수 공식 : (a종류의 개수) * (b종류의 개수) * (c종류의 개수) ...
    # 안입어도 되는 경우가 있기때문에 각 종류의 개수에 +1
    # 다 안입는 경우는 빼야하기때문에 전체에서 -1
    count = 1
    for k in wear_dict.keys():
        count *= (len(wear_dict[k])+1)
    
    print(count-1)