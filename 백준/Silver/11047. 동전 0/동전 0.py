n, k = map(int, input().split())
nList = []
num = 0
for i in range(n):
    nList.append(int(input()))
for i in range(n - 1, -1, -1):
    if k == 0:
        break
    if nList[i] > k:
        continue
    num += k // nList[i]
    k %= nList[i]
print(num)