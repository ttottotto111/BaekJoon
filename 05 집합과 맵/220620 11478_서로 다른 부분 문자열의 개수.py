import sys

s = sys.stdin.readline().rstrip()

result = set()
for i in range(1,len(s)+1):
    for j in range(0, len(s)-(i-1)):
        result.add(s[j:j+i])

print(len(result))