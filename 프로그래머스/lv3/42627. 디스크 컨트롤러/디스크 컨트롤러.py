'''
- 현시점에서 실행할 수 있는 프로세스 중 최소소요 시간 택
- 소요시간 = (이전 프로세스 소요시간 + 내 소요시간 - 요청시간)
- 현 프로세스 작업 후 -> 현시간 갱신 -> 현 시점에서 실행가능한 프로세스들 우선순위 큐에 넣음(최소힙)
'''
import heapq

def solution(jobs):
    answer, now, i = 0, 0, 0 #총 걸린 시간 누적, 현 시점, 작업 완료한 프로세스 개수
    start = -1 # 이전 프로세스 시점
    l = len(jobs)
    heap = []
    
    # 모든 프로세스 돌았으면 끝
    while i < l:
        # 현시점에 실행가능한 프로세스 최소힙 삽입
        for j in jobs:
            if start < j[0] <= now: # 이전 프로세스 이후에 온 것 부터 현 시점 이전에 온 것까지 삽입
                heapq.heappush(heap, (j[1], j[0])) #(소요시간, 요청시점) 순으로 삽입 - 소요시간 기준 최소힙 생성
        
        # 가장 덜 걸리는 다음 프로세스 추출
        if heap:
            p = heapq.heappop(heap)
            start = now # 이전 시점 갱신
            now += p[0] # 현시점 갱신
            i += 1 #프로세스 개수 갱신
            
            #요청부터 종료까지 걸린 시간
            answer += now - p[1] # now(= 이전 프로세스 소요시간 + 내 소요시간) - 요청시점
        else:
            # 힙이 비어있으면 시간 + 1
            now += 1
        
    return answer // l