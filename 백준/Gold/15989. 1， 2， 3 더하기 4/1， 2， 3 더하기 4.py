'''
n을 1, 2, 3의 합으로 나타내는 방법의 수 -> DP
- dp[1], dp[2], dp[3],..모두 집합으로 만들어서 튜플형태로 삽입

고민
- 1작은 수에 대해서는 dp 안하는 이유 = 계산해보니까, 2작은 수, 3작은 수와 모두 겹침.
'''
import sys
input = sys.stdin.readline

t = int(input())

# n<=10000, dp[n] == n이 되는 방법의 수
dp = [1] * 10001 # 1로만 n을 만드는 경우 먼저 추가

# 2작은 수
for i in range(2, 10001):
    dp[i] += dp[i-2]

# 3작은 수
for i in range(3, 10001):
    dp[i] += dp[i-3]

for _ in range(t):
    n = int(input())
    print(dp[n])