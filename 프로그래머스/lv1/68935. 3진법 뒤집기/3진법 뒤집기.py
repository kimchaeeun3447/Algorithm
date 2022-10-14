def solution(n):
    s = ''
    
    #3진법으로 바꾸기
    while n > 2:
        n, rest = divmod(n, 3)
        s += str(rest)
    s += str(n)
    
    #3진수 10진수로 바꾸기
    answer = int(s, 3) 
    
    return answer