def solution(numbers, target):
    answer = 0
    
    length = len(numbers) # 0~length-1까지 숫자 존재
    
    def dfs(idx, total):
        nonlocal answer
        if idx + 1 >= length:
            if total == target:
                answer += 1   
            return
    
        dfs(idx + 1, total + numbers[idx + 1])
        dfs(idx + 1, total - numbers[idx + 1])
    
    dfs(-1, 0)
        
    return answer