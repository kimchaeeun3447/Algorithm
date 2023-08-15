import math

def solution(progresses, speeds):
    answer = []
    _progresses = [] #완성하는데 걸리는 일수
    front = 0
    
    #두 리스트 한 번에 루프 돌리기
    for a, b in zip(progresses, speeds):
        _progresses.append(math.ceil((100 - a) / b))

    for i in range(len(_progresses)):
        if _progresses[i] > _progresses[front]:  
            answer.append(i - front)
            front = i
            
    answer.append(len(_progresses) - front)  

    return answer