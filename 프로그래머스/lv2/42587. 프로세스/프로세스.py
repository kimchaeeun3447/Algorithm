'''
- 주의: 이 부분이 잘 이해가 안됐음.
6개의 프로세스 [A, B, C, D, E, F]가 대기 큐에 있고 중요도가 [1, 1, 9, 1, 1, 1] 이므로 [C, D, E, F, A, B] 순으로 실행됩니다.
따라서 A는 5번째로 실행됩니다.
-> 9 앞에있는 2개의 1은 둘다 9보다 작으니까 pop이후에 다시 큐에 append하기땜에 이 순서로 실행됨

- any(조건) -> 리스트에서 조건 만족하는 게 있으면 True 반환
'''
from collections import deque

def solution(priorities, location):
    answer = 0
    queue = deque()

    for idx, p in enumerate(priorities):
        queue.append((p, idx))

    while queue:
        cur = queue.popleft()
        
        #큐 순서대로 pop하되, 우선순위 높은게 발견되면 다시 삽입
        # priorites가 최대 100개여서 괜찮음
        if any(cur[0] < p[0] for p in queue):
            queue.append(cur)
        else:
            # 자신이 우선순위 가장 높으면
            answer += 1
            if cur[1] == location:
                return answer