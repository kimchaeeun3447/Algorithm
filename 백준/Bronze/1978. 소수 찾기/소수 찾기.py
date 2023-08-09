import sys
input = sys.stdin.readline
n = int(input())

# 소수 찾기 - 에라토스테네스 체
a = set(map(int, input().split()))
end = max(a)

a -= {1}

for i in range(2, int(end ** 0.5) + 1):
    if a:
        a -= set(range(i * 2, max(a) + 1,i))

print(len(a))
