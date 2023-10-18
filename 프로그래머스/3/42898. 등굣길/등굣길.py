'''
갈 수 없는 곳 puddles -> puddles에 존재하는 경로가 아닐 경우에만 지날 수 있음
최단경로의 개수니까 -> 모든 경로 탐색해야함

- HOW?
물웅덩이(-1)일 경우 다른 곳에서 -1을 더하게되면 안되니까 0으로 바꾸고, continue => 어차피 이후에 지날 일 없음.
왼쪽, 위 칸에 저장된 최단 경로값을 더한게 현재 칸까지 오는데 필요한 경로값
'''

def solution(m, n, puddles):    
    dp = [[0] * (m + 1) for _ in range(n + 1)] # n행 m열
    dp[1][1] = 1 #집
    
    #물 웅덩이 -> -1로 표시
    for col, row in puddles:
        dp[row][col] = -1
    
    # m,n은 100이하의 자연수임
    for a in range(1, n + 1):
        for b in range(1, m + 1):
            # 물웅덩이(-1)일 경우 다른 곳에서 -1을 더하게되면 안되니까 0으로 바꾸고, continue => 어차피 이후에 지날 일 없음.
            if dp[a][b] == -1:
                dp[a][b] = 0
                continue
                
            #왼쪽, 위 칸에 저장된 최단 경로값을 더한게 현재 칸까지 오는데 필요한 경로값
            dp[a][b] += dp[a][b-1] + dp[a-1][b]
    
    print(dp)
    return dp[n][m] % 1000000007