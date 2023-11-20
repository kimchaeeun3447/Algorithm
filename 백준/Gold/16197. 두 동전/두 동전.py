'''
- 최소한의 이동 횟수니까 bfs 사용하기
- 떨어지려면 = 인덱스를 넘어가는 곳에 가야함
'''
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
coins = [0] # 버튼 횟수, 동전 1, 2 위치 넣기 [0, 3, 0, 4, 0]

# nxm 보드
graph = []

for i in range(n):
    graph.append(list(input().rstrip()))
    graph[i].append('.')
    
    for k in range(m):
        if graph[i][k] == 'o':
            coins.append(i)
            coins.append(k)

graph.append(list('.' * m))

# . 또는 o이면 이동가능, #이면 머무르기, 인덱스 벗어나면 낙오
'''
- 두 동전은 동시에 같이 움직임
- 두 동전이 동시에 낙오되면 그 루트는 끝
- 두 동전을 떨어뜨릴 수 없거나, 버튼을 10번보다 많이 눌러야 한다면, -1을 출력한다.
- 둘 중 하나만 낙오되면 return
'''
def bfs():
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    queue = deque([coins])
    
    while queue:
        cnt, x1, y1, x2, y2 = queue.popleft()

        # 버튼 10번 초과했으면
        if cnt > 10:
            break

        # 크게 4가지 케이스 발생 - 보드 판 내부 / 둘중 하나만 낙오됨 / 둘다 낙오됨
        
        if 0 <= x1 < n and 0 <= y1 < m and 0 <= x2 < n and 0 <= y2 < m:
            # 1) 모두 범위 내에 있다면
            for i in range(4):
                nx1, ny1 = x1 + dx[i], y1 + dy[i]
                nx2, ny2 = x2 + dx[i], y2 + dy[i]

                # 벽이면 원상복귀
                # 인덱스가 n이 되어도 오류가 나지않게 하기위해, 위에서 graph n+1, m+1로 초기화함
                if graph[nx1][ny1] == '#':
                    nx1, ny1 = x1, y1
                if graph[nx2][ny2] == '#':
                    nx2, ny2 = x2, y2

                queue.append((cnt + 1, nx1, ny1, nx2, ny2))
                
        elif 0 <= x1 < n and 0 <= y1 < m:
            # 2) 동전2가 낙오됨
            return cnt
        elif 0 <= x2 < n and 0 <= y2 < m:
            # 2) 동전1가 낙오됨
            return cnt
        else:
            # 3) 둘다 낙오됨
            continue

    return -1

print(bfs())