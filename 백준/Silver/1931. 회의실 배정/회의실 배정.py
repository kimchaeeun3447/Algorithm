import sys

n = int(input())

time = [[0]*2 for _ in range(n)]

for i in range(n):
    start, end = map(int, sys.stdin.readline().rstrip().split())
    time[i][0] = start
    time[i][1] = end

time.sort(key = lambda x: (x[1], x[0]))

cnt = 1 #time[0]
endTime = time[0][1]

for i in range(1, n):
    if time[i][0] >= endTime:
        cnt += 1
        endTime = time[i][1]

print(cnt)
