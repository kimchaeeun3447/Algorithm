import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(v):
    visited[v] = True

    # 인접 노드이고 && 아직 방문하지 않았다면 ->  dfs 실행
    for i, j in enumerate(graph[v]):

        if j and not visited[i]:
            dfs(i)

# 연결요소 = 하나의 연결된 component, 그래프에서 여러개의 component가 있을 수 있음
n, m = map(int, input().split()) # 정점개수 n / 간선개수 m


#dfs하고 더이상 갈곳없으면 요소 count +=1
# 1번 노드 ~ n번 노드 각각에 인접한 정점만 True  -> 인접 노드만 append하는 방법도 있음
graph = [[False] * (n+1) for _ in range(n+1)]

# 방문 노드 표시
visited = [False] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True


# 모든 노드에 대해 dfs 돌며, dfs 실행 시 결과 +1 / dfs 할게 없으면 pass
result = 0
for i in range(1, n+1):
    # if 이미 방문된 노드 -> pass
    # 방문 전 노드면 -> +1 한다. 어차피 얘 기준으로 dfs가 이루어질 것이니까
    if not visited[i]:
        dfs(i)
        result += 1
    
print(result)
