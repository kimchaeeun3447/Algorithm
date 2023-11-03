import sys
input = sys.stdin.readline

n = int(input()) #수열크기
nums = list(map(int, input().split())) #수열

dp = [k for k in nums] # dp[i] == i번쨰 인덱스까지의 부분 증가 수열중 가장 큰 합 저장

for cur in range(1, n):
    for before in range(cur):
        # 내 앞에 있는 값이 나보다 작을 경우에만 (증가수열이니까)
        if nums[before] < nums[cur]:
            # 더 큰 합을 dp에 저장 : 이전값까지의 dp에 현재값만 더하기 or 현재까지 갱신된 dp
            dp[cur] = max(dp[before] + nums[cur], dp[cur])

print(max(dp))
