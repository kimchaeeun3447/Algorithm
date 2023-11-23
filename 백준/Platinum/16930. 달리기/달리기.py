from collections import deque
import sys
input = sys.stdin.readline

def bfs(x1, y1, x2, y2):
    queue = deque([(x1, y1)])
    graph[x1][y1] = 0

    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

    while queue:
        x, y = queue.popleft()

        if x == x2 and y == y2:
            return graph[x][y]

        for i in range(4): #상하좌우
            nx, ny = x, y

            for _ in range(k): #현 방향에서 k번 이동 가능
                nx += dx[i]
                ny += dy[i]

                # 범위 벗어날 경우
                if nx < 0 or ny < 0 or nx >= n or ny >= m:
                    break

                # 이동할 수 없는 경우 - 벽
                if graph[nx][ny] == '#':
                    break

                # 어느 방향부터 탐색하느냐에 따라 최소값이 다르게 나올 수 있기 때문에, 중복방문가능
                # 이동할 수 있는 경우 - 첫 방문 or 중복방문 시 - 현재에서 이동하는게 기존시간보다 적게 걸리면 갱신함
                if graph[nx][ny] == '.':
                    queue.append((nx, ny))
                    graph[nx][ny] = graph[x][y] + 1 #시간은 시작점기준으로 1초만 더함 : 1~k개 이동가능하니까
                elif graph[nx][ny] > graph[x][y]:
                    # 중복 방문 시 -> 큐에 또 삽입하는게 아니라  break를 안하고, continue를 해서 계속 그 방향으로 탐색한다.
                    continue
                else:
                    # 현재 방향으로 가면 더 오래걸릴 경우
                    break

    return -1

n, m, k = map(int, input().split())

# 벽 -1 / 아직 방문x 0으로 표시 / 방문하면 최소 시간 저장
graph = [list(input()) for _ in range(n)]

x1, y1, x2, y2 = map(int, input().split())

print(bfs(x1-1, y1-1, x2-1, y2-1))