import sys
from collections import deque 

n, k = map(int, sys.stdin.readline().split())
visited = [0] * 100001 #visited[i] = i까지 오는데 걸린 최소 시간
cnt = 0 # 경우의 수

'''
- 가장 빠른 시간이 몇 초 후인지 그리고, 가장 빠른 시간으로 찾는 방법이 몇 가지 인지 구하기
- 가장 빠른 경로 구해야되니까 최단경로 BFS 사용
- 최소 시간과 동일한 모든 경로 찾아야함 -> 최소 시간 넘어가면 안됨

최소시간 안에 오는 경로만 누적하는 로직 :
- 현재에서 1초 후에 최소시간안에 x에 도달할 수 있는 경우에만 cnt + 1
'''

queue = deque()
queue.append(n)

while queue:
    cur = queue.popleft() #(현재 숫자, 걸린 시간)

    if cur == k:
        cnt += 1
        continue

    for next in [cur - 1, cur + 1, cur * 2]:
        if 0 <= next <= 100000:
            
            # 범위 내의 숫자이면서 and (처음 도달한 곳인지 or 이전에 도달한 곳인지)
            if visited[next] == 0:
                visited[next] = visited[cur] + 1 #최소시간 저장
                queue.append(next)
                
            elif visited[next] == visited[cur] + 1: #현재에서 1초만 있으면 도달할 수 있다면==최소시간이 동일하게 도착가능하다면
                queue.append(next)
                
print(visited[k])
print(cnt)