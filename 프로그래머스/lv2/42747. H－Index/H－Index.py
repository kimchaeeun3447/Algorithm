def solution(citations):
    
    citations.sort()
    
    
    #citations 길이 = 논문 개수
    #[1, 2, 3] -> 1번째 논문의 인용개수 = 2 / 0, 1번째까지는=2편은 2번이상 인용된것
    c_total = len(citations) # 논문 총 개수
    
    for c_idx, c in enumerate(citations):
#         c_count = sum(1 for num in citations if num >= c)
        
#         if c <= c_count:
#             answer = c
#             break
        if c >= c_total - c_idx:
            return c_total - c_idx
        
    return 0