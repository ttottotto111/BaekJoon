import sys

p = sys.stdin.readline().rstrip()

# ppap용 스택
ppap = []

for s in p:
    ppap.append(s)
    
    if len(ppap) >= 4 and ppap[-4:] == ["P","P","A","P"]:
        ppap.pop()
        ppap.pop()
        ppap.pop()

if ppap == ["P","P","A","P"] or ppap == ["P"]:
    print("PPAP")
else:
    print("NP")