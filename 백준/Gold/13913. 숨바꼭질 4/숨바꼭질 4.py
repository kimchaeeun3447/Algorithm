from collections import deque

'''
가장 빠르게 찾을 수 있는 시간 -> 최단 경로 찾기 BFS
'''
n, k = map(int, input().split())
queue = deque([(n, 0)]) #bfs 큐에 (x, 누적 시간) 저장

visited = [-1] * 100001 # visited[현재위치] = 바로 이전의 위치
visited[n] = n

while queue:
    x, t = queue.popleft()

    if x == k:
        print(t) #최단 시간
        break

    for next in (x - 1, x + 1, x * 2):
        # 범위 내의 숫자이고, 아직 방문한 적없는 위치일 경우에만 큐에 넣기
        # 방문한 곳을 또 방문하면 최단경로가 되지 않음!
        if 0 <= next <= 100000 and visited[next] == -1:
            queue.append((next, t + 1))
            visited[next] = x

# 최단 경로 - k번째부터 visited에 저장된 바로 이전의 위치를 출력
idx = k
path = [k]

while idx != n:
    path.append(visited[idx]) # 이전 위치 경로에 넣기
    idx = visited[idx]

print(*path[::-1])