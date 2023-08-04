import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split())) #수열
s = [a[0]] #누적합

# (나까지 연속하는게 더 큰 수의 합이 될 경우=내 앞에서 만들어진 최댓값 + 나)
# or (나 혼자가 앞의 연속된 합에 더하는 것보다 클 경우 ex)음수시작)
# 가장 큰 합을 계속 append하기
for i in range(1, n):
    s.append(max(s[-1] + a[i], a[i]))

print(max(s))