'''
- 트럭이 선입선출로 나가니까 큐를 사용함
- 최대 트럭 개수 유지법 = 1개 pop하고 무조건 1개 append하는 로직이기때문에 가능
'''
from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0

    #다리를 건너는 트럭
    queue = deque([0] * bridge_length) #최대 트럭개수만큼 빈칸 만들어둠
    
    #무게 누적
    cur_weight = 0

    while queue:
        cur_weight -= queue.popleft()
        answer += 1

        if truck_weights:
            if cur_weight + truck_weights[0] <= weight:
                #새로 트럭이 들어와도 되는 경우
                cur_truck = truck_weights.pop(0)
                queue.append(cur_truck)
                cur_weight += cur_truck
            else:
                #새로 트럭이 들어올 수 없는 경우 빈자리만 추가
                queue.append(0)
        
    return answer