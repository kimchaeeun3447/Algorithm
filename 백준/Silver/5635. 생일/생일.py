A = []
for _ in range(int(input())):
    n, d, m, y = input().split()
    A.append([n, int(d), int(m), int(y)])
A.sort(key=lambda x:(x[3],x[2],x[1]))
print(A[-1][0])
print(A[0][0])