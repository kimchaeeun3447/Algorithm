def solution(nums):
    # 최대 가질수있는 종류수 / 실제 종류수
    m, k = len(nums) // 2, len(set(nums))
    answer = k if m >= k else m
    
    return answer