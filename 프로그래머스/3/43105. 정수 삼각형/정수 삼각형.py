'''
자신이 [a][b] 인덱스면 -> [a+1][b] 또는 [a+1][b+1]로만 이동이 가능함
-> dp[a][b] 에는 dp[a-1][b] 또는 dp[a-1][b-1] 중에 더 큰 값을 더함
'''

def solution(triangle):
    answer = 0
    row, col = len(triangle) + 1, len(triangle[-1]) + 1
    
    dp = [[0] * col for _ in range(row)]
    
    for r_idx, r in enumerate(triangle):
        for c_idx, c in enumerate(r):
            dp[r_idx + 1][c_idx + 1] = c
    
    for a in range(1, row):
        for b in range(1, col):
            dp[a][b] += max(dp[a-1][b], dp[a-1][b-1])
    
    return max(dp[-1])