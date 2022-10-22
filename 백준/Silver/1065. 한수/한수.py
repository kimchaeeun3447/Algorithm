def bigger_count(n):
    cnt = 0
    for num in range(100, n+1):
        if num >= 100:
            before = 0 # 비교할 수
            for _ in range(2):
                num, remainder = divmod(num, 10)
                diff = before - remainder #등차
                before = remainder
    
            while (num!=0):
                num, remainder = divmod(num, 10)
                if (before - remainder) != diff:
                    break
            else:
                cnt += 1
    return cnt

num = int(input())
count = 0

if num < 100:
    count += num
else:
    count += 99 + bigger_count(num)

print(count)
