'''
자신이 [a][b] 인덱스면 -> [a+1][b] 또는 [a+1][b+1]로만 이동이 가능함
-> dp[a][b] 에는 dp[a-1][b] 또는 dp[a-1][b-1] 중에 더 큰 값을 더함
'''

def solution(triangle):        
    for r_idx, r in enumerate(triangle):
        r_length = len(r)
        
        for c_idx, c in enumerate(r):
            # 1행 부터 dp실행
            if r_idx == 0:
                continue
            
            # 0열은 우측 대각선 상단 값만 / 마지막 열은 좌측 대각선 상단 값만 / 그외는 둘 중 더 큰값이 옴
            if c_idx == 0:
                triangle[r_idx][c_idx] += triangle[r_idx-1][c_idx]
            elif c_idx == r_length - 1:
                triangle[r_idx][c_idx] += triangle[r_idx-1][c_idx-1]
            else:
                triangle[r_idx][c_idx] += max(triangle[r_idx-1][c_idx], triangle[r_idx-1][c_idx-1])
    
    
    return max(triangle[-1])