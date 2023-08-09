import sys
input = sys.stdin.readline
t = int(input())

for _ in range(t):
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    print(a[2])
