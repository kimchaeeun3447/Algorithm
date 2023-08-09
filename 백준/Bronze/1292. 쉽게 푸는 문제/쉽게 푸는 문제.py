a,b = map(int,input().split())
 
arr = [0]
for i in range(46): #a, b의 범위는 1,000이기때문에 46까지만 수열 구함
    for _ in range(i):
        arr.append(i)
 
print(sum(arr[a:b+1]))
