'''
- 다음으로 이동하는 방법 : 상하좌우 칸 중 벽이 없는 곳
- 고민 : 이동가능한 칸이 여러개일때 어디가 최단경로인지 판단
-> 각각 경로에 대해 따로 bfs를 실행해서 결과중에 min값 찾기

각 칸까지 오는데 걸린 칸수를 저장하면, 자동으로 더오래걸린 길은 도착지로 가기전에 1인 칸이 없으니까 stop됨
'''
from collections import deque

def solution(maps):
    dx, dy = [-1, 1, 0, 0], [0, 0, 1, -1] # 상하좌우
    
    queue = deque([(0, 0)]) #다음으로 이동할수있는 좌표
    
    while queue: #이동할곳이 없을때까지
        x, y = queue.popleft() #현위치
        
        #다음으로 이동할 수 있는 좌표 탐색
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            # 접근가능한 지점인지 확인
            if nx < 0 or ny < 0 or nx >= len(maps) or ny >= len(maps[0]):
                continue
            
            # 벽이 있는지 or 이미 최단경로로 지난 곳이 아니면 다음 코스로 삽입
            if maps[nx][ny] == 1:      
                queue.append((nx, ny))
                maps[nx][ny] = maps[x][y] + 1 #경로 누적
    
    #(n,m) 값이 1이라면 도달못한 것이므로 -1 반환
    answer = maps[-1][-1]
    if answer == 1:
        return -1
    else:
        return answer