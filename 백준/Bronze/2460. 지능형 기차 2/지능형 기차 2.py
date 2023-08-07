# [누적된 탄 사람] = [누적된 탄 사람] - 현재역의 내린 사람 수 + 현재역에 탄 사람 수
total = 0 #누적
max_total = 0

for i in range(1, 11):
    a, b = map(int, input().split())

    now = total - a + b
    
    max_total = now if now > max_total else max_total
    total = now


print(max_total)