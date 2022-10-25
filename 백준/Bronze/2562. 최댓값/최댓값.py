a = []
for _ in range(9):
    a.append(int(input()))
m = max(a)
print(m)
print(a.index(m) + 1)