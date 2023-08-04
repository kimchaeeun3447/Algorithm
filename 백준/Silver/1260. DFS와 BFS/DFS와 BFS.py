import sys
from collections import deque
input = sys.stdin.readline

n, m, v = map(int, input().split()) # 노드 수 n / 간선 수 m / 탐색 시작 노드번호 v


# 그래프 - 노드번호(행 번호), 인접한 노드 번호(열 번호) True 표시
graph = [[False] * (n+1) for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split()) # 인접한 노드 번호 a, b

    #인접함 = True로 표시
    graph[a][b] = True
    graph[b][a] = True

''' ex)
graph = [
    [FALSE, FALSE, FALSE, FALSE],
    [FALSE, TRUE, FALSE, FALSE],
    [FALSE, TRUE, FALSE, FALSE],
    [FALSE, TRUE, FALSE, FALSE]

]
'''

# 방문노드 표시
visited_dfs = [False] * (n+1)
visited_bfs = [False] * (n+1)


#DFS
def dfs(v):
    # 현재 노드 방문 처리
    visited_dfs[v] = True
    print(v, end=" ")

    # 현재 노드 i의 인접노드들에 대해 DFS 호출 - 인접노드이면서 && 방문하지 않았으면 방문처리
    for i in range(1, n+1):
        if graph[v][i] and not visited_dfs[i]:
            dfs(i)
        

#BFS
def bfs(v):
    # 큐 생성
    queue = deque([v])
    # 현재 노드 방문 처리
    visited_bfs[v] = True

    # 큐가 빌 때까지 - 원소 popleft해서, 해당 노드번호의 인접노드 모두 큐에 삽입 후 -> 방문처리
    while queue:
        v = queue.popleft()
        print(v, end=" ") # pop할 때 출력
        
        for i in range(1, n+1):
            if graph[v][i] and not visited_bfs[i]:
                queue.append(i)
                visited_bfs[i] = True

# 실행
dfs(v)
print()
bfs(v)



