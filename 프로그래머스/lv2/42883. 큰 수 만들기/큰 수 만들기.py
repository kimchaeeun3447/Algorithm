def solution(number, k):
    answer = [] # 스택
    
    for n in number:
        #큰수가 앞자리에 오게하기 위해 while루프로 pop
        while answer and k > 0 and answer[-1] < n:
            answer.pop()
            k -= 1
        answer.append(n)
    
    return ''.join(answer[:len(answer) - k])