import sys
from itertools import combinations

input = sys.stdin.readline

for i in list(combinations([int(input()) for _ in range(9)], 7)):
    if sum(i) == 100:
        print(*sorted(i), sep = '\n')
        break