'''
우선순위대로 계속 정렬해야하는 문제니까 => 힙 정렬 사용하자
- 스코빌 지수 기준 최소 힙 생성 -> 가장 작은 값 2개 pop -> 섞은 음식으로 가공 후 push
- 모든 음식이 k이상이 될때까지 반복 = 루트 노드가 K이상이 될때까지

'''
import heapq

def solution(scoville, K):
    answer = 0
    
    # 최소 힙 생성
    h = []
    for s in scoville:
        heapq.heappush(h, s) 
    
    while len(h) > 1:
        m = heapq.heappop(h)
        if m >= K: #루트 노드가 K이상이 될 때까지
            break
        
        heapq.heappush(h, m + heapq.heappop(h) * 2)
        answer += 1
    
    # 모든 음식의 스코빌 지수를 K 이상으로 만들 수 없는 경우
    if heapq.heappop(h) < K:
        return -1
    
    return answer