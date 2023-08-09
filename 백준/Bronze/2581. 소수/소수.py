m, n = int(input()), int(input())

a = set(range(m, n + 1)) - {1}

for i in range(2, int(n ** 0.5) + 1):
    if a:
        a -= set(range(i * 2, max(a) + 1, i))

if not a:
    print(-1)
else:
    print(sum(a))
    print(min(a))