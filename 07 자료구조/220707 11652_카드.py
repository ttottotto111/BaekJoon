import sys

n = int(sys.stdin.readline().rstrip())

num_dict = dict()

for _ in range(n):
    num = int(sys.stdin.readline().rstrip())
    if num in num_dict:
        num_dict[num] += 1
    else:
        num_dict[num] = 1

result = sorted(num_dict.items(), key = lambda x:(-x[1],x[0]))
print(result)