import sys

N = int(sys.stdin.readline().strip())
times = list(map(int, sys.stdin.readline().strip().split()))
total = 0

times.sort()
for idx in range(N):
    total += sum(times[0:idx+1])
print(total)

    
    