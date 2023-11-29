import sys
input = sys.stdin.readline

sys.setrecursionlimit(10**9) # 재귀에서 이거 써야 recursion error 막음

n = int(input()) # 정점 n개
graph = [[] for _ in range(n + 1)]
dp = [[0, 0] for _ in range(n + 1)] # [자신이 0인경우, 1인경우]

for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n + 1) #방문유무

# 트리를 DFS하며 DP하는 로직
def dfs(cur, dp):
    visited[cur] = True # 현재 노드 방문처리

    #자식 노드에 대해 dfs 탐색 = 서브트리 먼저 수행하고 와서 현재 노드 값 결정
    for v in graph[cur]:
        if not visited[v]: # leaf 노드는 부모가 이미 visited된 후 호출되니까 여기 건너뜀
            dfs(v, dp) #자식 노드(루트노드) 먼저 탐색

            # 현재노드가 0일때 -> 자식노드 무조건 1이어야함.
            dp[cur][0] += dp[v][1]

            # 현재 노드가 1일 때 -> 자식노드 값 상관 x, 둘중 최소값 저장하기
            dp[cur][1] += min(dp[v][0], dp[v][1])

    #모든 자식노드들에 대해서 최소값을 저장했으니, 자신이 1일경우에만 1개 더해주기
    # 자식노드가 여러개면, 그 작업을 모두 처리한 후에 자기자신 1개를 더해야함
    dp[cur][1] += 1

dfs(1, dp) #1번 노드부터 DFS 시작

# 루트 노드 1을 골랐을 때 or 안골랐을 때 중 더 적은 노드가 사용되는 경우 선택
print(min(dp[1][0], dp[1][1]))