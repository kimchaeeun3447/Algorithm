x = int(input())
for i in range(x):
    y = input()
    s = list(y)
    sum = 0
    z = 1
    for i in s:
        if i == 'O':
            sum += z
            z += 1
        else:
            z = 1
    print(sum)