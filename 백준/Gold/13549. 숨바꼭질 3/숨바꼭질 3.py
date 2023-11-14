from collections import deque

n, k = map(int, input().split())

queue = deque([n])
visited = [-1] * 100001 # visited[현재위치] = 현재까지 걸린 최단 시간, 한번도 간적없으면 -1
visited[n] = 0

while queue:
    x = queue.popleft()

    if x == k:
        print(visited[x])
        break

    for next in (x-1, x+1, x*2):
        # 아직 한번도 안간 위치일 경우에만 지남
        if 0 <= next < 100001 and visited[next] == -1:
            if next == x*2:
                # 0초 걸리는 경우는 맨앞에 추가해준다
                queue.appendleft(next)
                visited[next] = visited[x]
            else:
                queue.append(next)
                visited[next] = visited[x] + 1