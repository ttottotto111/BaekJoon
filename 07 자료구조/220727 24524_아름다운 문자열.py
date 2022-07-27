import sys

s = sys.stdin.readline().rstrip()
t = sys.stdin.readline().rstrip()

# 비교할 문자열
str_count = [0 for _ in range(len(t))]
t_set = set(t)
count = 0

# 문자열을 한개씩 반복
for i in s:
    # 문자가 t에 있을경우
    if i in t_set:
        # 문자가 t의 첫번째 문자와 같을경우
        # 문자 카운트용 리스트 첫번째값 +1
        if i == t[0]:
            str_count[0] += 1
        
        # 문자가 t의 첫번째 문자가 아닐경우
        # t에서 문자 i의 위치 index에 저장
        else:
            index = t.find(i)
            
            # 현재 문자의 바로 전 문자가 이미 있을경우 : 연속된 문자가 t문자열과 같을경우
            # 이전 문자 -1, 현재문자 +1 : 기존문자열에서 비교할 t문자열을 뺀다는 의미
            # 문자 카운트 리스트의 가장 마지막 값이 결과값 (나온 문자열의 총 개수)
            if str_count[index-1]:
                str_count[index-1] -= 1
                str_count[index] += 1

print(str_count[-1])