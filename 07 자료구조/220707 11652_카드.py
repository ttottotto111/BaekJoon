import sys

n = int(sys.stdin.readline().rstrip())

num_dict = dict()

for _ in range(n):
    num = int(sys.stdin.readline().rstrip())
    if num in num_dict:
        num_dict[num] += 1
    else:
        num_dict[num] = 1

# value 값으로 내림차순 정렬, 같다면 key값으로 오름차순 정렬
result = sorted(num_dict.items(), key = lambda x:(-x[1],x[0]))
print(result[0][0])