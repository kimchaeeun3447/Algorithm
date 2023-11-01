'''
- 집이 최대 1000000개
- 인덱스가 짝수번째, 홀수번째 중 어떤것을 더하는게 좋을지 모르기 떄문에, dp로 계속 이전값과 현재값을 비교하며 최대값을 저장해야한다.

[로직]
- max(1) i-1번째까지의 dp 그대로, 2) i-2번째 까지의 dp에 i번째(현재)값을 더하는 것)
위의 1), 2) 중 더 큰 값을 i번째까지의 dp에 넣는다. 이렇게하면 현재값을 포함할지, 아니면 건너뛸지 정해짐
- 1)의 경우 i번째는 건너뛴다는 뜻, 2의 경우 i번째를 포함한다는 뜻이다.

- dp를 0번째에서 시작할 경우와 1번째에서 시작할 경우로 나눠야함. 시작 인덱스에 따라 마지막 인덱스를 포함할 수 있는지 없는지가 정해지기 떄문.

- dp[i]의 의미 = i번째 인덱스까지의 최대 누적값
'''
def solution(money):
    answer = 0
    
    end = len(money) - 1
    
    dp1 = [] # 0번째 방문 DP -> 마지막 인덱스 포함 불가
    dp2 = [] # 1번째 이후 방문 DP -> 마지막 인덱스 포함 가능
    
    # dp1 - 0번째 인덱스 방문, 1번째 인덱스 방문x
    dp1.append(money[0])
    dp1.append(dp1[0])
    
    # dp2 - 0번째 인덱스 방문x, 1번째 인덱스 방문
    dp2.append(0)
    dp2.append(money[1])
    
    
    # 2번째 인덱스부터 ~ 마지막-1 인덱스까지 최대값 저장 : i-1까지의 dp 그대로 가져가고 현재 i는 포함 x OR i-2까지의 dp에 현재 i 포함 o
    for i in range(2, end):
        dp1.append(max(dp1[i-1], dp1[i-2] + money[i]))
        dp2.append(max(dp2[i-1], dp2[i-2] + money[i]))
    
    
    # dp1은 마지막 인덱스 포함 불가니까 dp[마지막-1]이 최대, dp2는 마지막 포함 유무에 따라 최대 dp값 저장
    dp1.append(dp1[end-1])
    dp2.append(max(dp2[end-1], dp2[end-2] + money[end]))
    
    return max(dp1[end], dp2[end])
