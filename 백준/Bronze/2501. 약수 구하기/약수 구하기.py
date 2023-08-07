n, k = map(int, input().split())

a = {1, n}

if n > 1:
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            a |= {i, n // i}

# 약수 개수 < k 이면 -> 0 출력, 아니면 정렬후 k-1번째 수 가져옴
print(0 if len(a) < k else sorted(a)[k-1])
