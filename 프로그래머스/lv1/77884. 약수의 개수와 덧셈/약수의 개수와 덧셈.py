def solution(left, right):
    answer = 0
    
    for num in range(left, right + 1):
        k = 2
        divisor_num = 0
        while (k < num):
            if num % k == 0:
                divisor_num += 1
            k += 1
            
        if num is not 1 and divisor_num % 2 == 0:
            answer += num
        else:
            answer -= num
    
    return answer