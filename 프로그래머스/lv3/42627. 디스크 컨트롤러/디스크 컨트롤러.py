'''
요청에서 종료까지 시간 = 이전 작업의 소요시간 - 자신의 작업요청시점 + 자신의 작업 소요시간

- 하드디스크가 작업을 수행하고 있지 않을 때에는 먼저 요청이 들어온 작업부터 처리합니다.

전체 작업시간을 줄이는 방법 : 현 시점에 처리가능한 작업중에서, 소요시간이 덜걸리는 작업 우선 처리
'''

import heapq

def solution(jobs):
    answer, now, i = 0, 0, 0
    start = -1 
    heap = []

    # 전체 작업개수만큼 반복
    while i < len(jobs):
        # 현재 시점에서 처리할 수 있는 작업을 heap에 저장
        for j in jobs:
            if start < j[0] <= now:
                heapq.heappush(heap, [j[1], j[0]])
        
        if len(heap) > 0: # 처리할 작업들이 있는 경우 - 제일 덜 걸리는 작업 처리
            current = heapq.heappop(heap)
            start = now
            now += current[0] #현재 작업 소요시간 추가
            answer += now - current[1] # 작업 요청시간 제거
            i +=1
        else: # 처리할 작업이 없는 경우 - 현재시간 + 1
            now += 1
                
    return answer // len(jobs)


print(solution([[0, 3], [1, 9], [2, 6]]))
