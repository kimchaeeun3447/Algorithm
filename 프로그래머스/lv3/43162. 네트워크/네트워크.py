'''
- 전력망을 둘로 나누기 문제랑 비슷한 듯?
- bfs로 네트워크 인접부분 찾다가 더이상 없으면 break
- 고민 포인트 : bfs 1텀끝나면 네트워크 +1이 됨, 그러면 다음 꺼는 언제?시작하나! = visited를 for문으로 돌며, 아직 방문안한 노드에 대해 bfs실행해봄
1시작, 2끝(answer=1) -> 3시작, 3끝(answer=2)
'''
from collections import deque

def solution(n, computers):
    answer = 0
    visited = [False] * n  #방문유무 표시
    
    def bfs(k):
        queue = deque([k]) #k부터 방문 시작
        visited[k] = True #방문처리
    
        #k와 인접한 노드 방문처리
        while queue:
            c = queue.popleft()
            
            for i in range(n):
                if computers[c][i] == 1 and not visited[i]:
                    queue.append(i)
                    visited[i] = True #방문처리
        
        nonlocal answer
        answer += 1 # 네트워크 개수 +1
                    
    for i in range(n):
        if not visited[i]:
            bfs(i)
    
    return answer