from collections import deque

s = int(input()) # s개의 이모티콘을 만들어야함

'''
[d에서 s가 되는 최소 시간 => bfs로 풀기]

이모티콘 로직 3개 -> 각 1초 걸림
1. 화면의 이모티콘 개수 만큼 클립보드에 저장 - 새로 저장할때마다 갱신됨 (c = d)
2. 클립보드 개수만큼 화면에 추가 (d + c)
3. 화면에 있는 이모티콘 1개 삭제 (d - 1)

1 -> 2 를 하게 되면 : 2초걸림, 화면에 있는 개수만큼 더 빨리 갱신 가능

- visited 리스트엔 각 이모티콘 개수가 되는데 걸린 최단시간을 저장함

- 고민1 : 클립보드에 저장된 개수를 큐에 같이 넣어줄지 or 따로 리스트 만들어서 갱신시킬지
일단 전자의 방법으로 시도

- 고민2 : 클립 보드 개수를 언제 갱신하면 좋을 지
갱신해도 범위 내일 경우 추가

'''
#방문 유무 visited[현이모티콘개수][현클립보드개수] 해야하는 이유 => 이모티콘 개수가 같아도 클립보드 개수 다르면 다른 케이스니까
visited = [[-1] * 1001 for _ in range(1001)] # s의 최대값은 1000, 걸린 최단시간
visited[1][0] = 0 # 시작시간 0초로 해두는거 까먹지 말기

queue = deque([(1, 0)]) # (현재 이모티콘 개수, 현재 클립보드 개수)

while queue:
    e, c = queue.popleft()

    if e == s:
        print(visited[e][c])
        break

    for i in range(3):
        if i == 0:
            next_e, next_c = e + c, c  #현이모티콘 + 클립보드 개수
        elif i == 1:
            next_e, next_c = e - 1, c # 현이모티콘 -1
        else:
            next_e, next_c = e, e # 클립보드 개수 = 현 이모티콘 개수로 갱신

        if 0 <= next_e <= 1000 and 0 <= next_c <= 1000 and visited[next_e][next_c] == -1:
            queue.append((next_e, next_c))
            visited[next_e][next_c] = visited[e][c] + 1 #시간 + 1