s = [0]

for i in range(10):
    a, b = map(int, input().split())
    s.append(s[i] - a + b)

print(max(s))