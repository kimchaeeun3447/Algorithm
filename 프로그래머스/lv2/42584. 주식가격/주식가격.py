'''
- 자신 이후(우측)의 자신보다 값이 더 작아지는 순간 초 세는 것을 스탑
- 이걸 스택/큐로 풀 만한 문제인가?!
'''

def solution(prices):
    answer = []
    l = len(prices)
    
    for idx, p in enumerate(prices):
        t = 0
        
        while t < l - idx -1:
            t += 1
            if prices[idx + t] < p:
                break
                
        answer.append(t)
    
    return answer