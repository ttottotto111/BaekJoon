import sys

n = int(sys.stdin.readline().rstrip())

book = dict()

for _ in range(n):
    name = sys.stdin.readline().rstrip()
    
    if name in book:
        book[name] += 1
    else:
        book[name] = 1

# 책의 개수로 내림차순정렬, 같을시 이름으로 사전순 정렬
result = sorted(book.items(), key=lambda x: (-x[1], x[0]))

print(result[0][0])