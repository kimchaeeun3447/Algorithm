import sys

n = int(sys.stdin.readline().rstrip())
sList = []

for i in range(n):
    sList.append(sys.stdin.readline().rstrip())
setList = set(sList)
sList = list(setList)
sList.sort()
sList.sort(key = len)

print(*sList, sep='\n')