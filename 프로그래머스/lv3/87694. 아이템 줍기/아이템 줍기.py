'''
- (characterX, characterY)에서 (itemX, itemY)까지 가는 최단경로
- 경로는 (상, 하, 좌, 우)에서 갈 수 있는 경로를 찾으며 이동
둘레 길 & 아직 지나지 않은 경로면 이동하기
- lv2 게임 맵 최단거리랑 비슷한 bfs 문제인듯

[풀이]
1) 주어진 rectangle들로 지날 수 있는 경로를 1로 만들기 -> 모르겠음
- 1. 51x51 배열을 2배로 늘린 102 x 102로 초기화
- 2. (x1, y1, x2, y2) -> x1~x2까지 y1~y2까지
모든 직사각형 좌표에서 다른 직사각형 범위와 겹치는 좌표는 pass됨.
= x1 < x좌표 < x2 and y1 < y좌표 < y2에 속해있으면 -> 지날 수 없음

1) 각 직사각형에 대해 테두리 좌표&다른 직사각형의 내부가 아니면(0이 아니면) -> 1로, 내부 좌표면 0으로 바꿔줌
-> 여기서 이해안되는거 좌표를 2배로 늘리는 이유! = 바로 위에 있는 좌표가 지나갈 수 있는 경로이더라도, 직사각형 특성상 좌표사이를 연결하는 테두리가 없다면 가지 못함. 그래서 좌표를 2배로 늘리고 시작하는 것임

2) (상, 하, 좌, 우)에서 갈 수 있는 경로를 찾으며 이동
'''

from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    
    #지날 수 있는 경로는 1, 직사각형 내부는 0으로 표시한 그래프
    graph = [[-1] * 102 for i in range(102)] # 50x50 배열 -> 상하좌우 탐색 시 range 관련 if문 안쓰기위해 51x51로 생성 -> 좌표를 2배로 늘려줌
    
    # graph에서 지나갈 수 있는 경로만 1로 표시
    # 각 직사각형에 대해 테두리는 1, 내부는 0으로 해두기 -> 테두리의 경우 0이 아닌 경우에만
    for r in rectangle:
        x1, y1, x2, y2 = map(lambda x: x * 2, r) #좌표 2배로 늘려줌
        
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                
                # 직사각형 내부 좌표라면 0
                if x1 < x < x2 and y1 < y < y2:
                    graph[x][y] = 0
                    
                # 테두리 좌표라면 -> 다른 직사각형의 좌표이지 않으면 1
                elif graph[x][y] != 0:
                    graph[x][y] = 1

    
    queue = deque([(characterX * 2, characterY * 2)])
    
    #방문한 경로에 대해서만 경로를 누적하는 그래프 - 방문안한 곳은 0로 표시
    visited = [[1] * 102 for i in range(102)]
    visited[characterX * 2][characterY * 2] = 0 # 시작지점 경로누적 0으로 수정
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
      
    while queue:
        x1, y1 = queue.popleft()
        
        # 도착점
        if x1 == itemX * 2 and y1 == itemY * 2:
            answer = visited[x1][y1] // 2
            break
        
        # 상하좌우 중에서 지날 수 있고 & 아직 방문안한 경로 탐색
        for i in range(4):
            x, y = x1 + dx[i], y1 + dy[i]
            
            if graph[x][y] == 1 and visited[x][y] == 1:
                queue.append((x, y))
                visited[x][y] = visited[x1][y1] + 1 #경로 누적
    
    return answer