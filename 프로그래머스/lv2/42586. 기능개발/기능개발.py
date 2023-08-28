import math

def solution(progresses, speeds):
    answer = []
    
    #각 작업이 100%되는 데 걸리는 시간 가공
    # 올림처리
    _progresses = []
    for p, s in zip(progresses, speeds):
        _progresses.append(math.ceil((100 - p) / s))

    front = 0 #앞쪽 비교대상

    for i in range(len(_progresses)):
        # front보다 커질 경우, front ~ i-1번째까지 삽입 = i-front 개
        if _progresses[front] < _progresses[i]:
            answer.append(i - front)
            front = i #i번째부터 다시 시작        

    answer.append(len(_progresses)- front)
    return answer

print(solution([95, 90, 99, 99, 80, 99], [1,1,1,1,1,1]))

#[5, 10, 1, 1, 20, 1]일 걸림
# 5 < 10 -> 5 (1개) -> [5, -4, -4, 15, -4]
# 5 > -4  & 5 > -4 / 5 < 15 -> 5, -4, -4 (3개) -> [10, -9]
# 10 > -9-> 10, -9(2개)