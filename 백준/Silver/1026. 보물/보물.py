import sys

N = int(input())
A = list(map(int, sys.stdin.readline().rstrip().split()))
B= list(map(int, sys.stdin.readline().rstrip().split()))

A.sort()
B.sort(reverse=True)

print(sum(map(lambda x, y: x*y, A, B)))