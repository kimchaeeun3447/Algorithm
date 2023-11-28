'''
- 알고리즘 : 위상정렬 + 복잡한 조건
방향그래프에 맞게 노드 방문해야하기 때문에 위상정렬이 사용됨

- 예시
    indegrees -> [-1, 0, 0, 2, 2, 1, 0, 3]
    outdegrees -> [[], [3], [3], [4, 5], [7], [7], [4, 7], []]
    queue -> [(1, 1), (1, 2), (1, 6), (2, 3), (2, 4), (2, 5), (3, 7)]
'''
from collections import deque
import sys
input = sys.stdin.readline

# Strahler 순서 결정 - 현재노드의 진입노드들의 Strahler에 따라 결정됨
# 1) indegree_seqs의 최대값 i  - 2) i가 1개면 -> 순서 = i, i가 2개이상 -> 순서 = i+1
def strahler_seq(v, indegree_seqs):
    i = max(indegree_seqs[v])

    if indegree_seqs[v].count(i) < 2:
        return i
    else:
        return i + 1


# 하천계의 최종적 Strahler 순서 출력 - 위상정렬
def topology_sort(v, indegrees, outdegrees):
    queue = deque() # 큐에 (Strahler 순서, 노드번호)을 삽입

    # 큐에 진입차수가 0인 노드 모두 삽입
    for i in range(v + 1):
        if indegrees[i] == 0:
            queue.append((1, i))

    # 노드 번호 별 진입노드의 Strahler 순서 저장
    indegree_seqs = [[] for _ in range(v + 1)]

    # 큐가 빌 때까지 현재 노드의 모든 진출 노드를 방문
    while queue:
        seq, cur = queue.popleft()

        for next in outdegrees[cur]:
            # 진출노드의 진입차수 1 감소
            indegrees[next] -= 1

            # 진입노드의 Strahler 순서 저장
            indegree_seqs[next].append(seq)

            # 해당 진출노드의 진입차수가 0이 되었다면, 큐에 추가
            if indegrees[next] == 0:
                # Strahler 순서 결정
                n_seq = strahler_seq(next, indegree_seqs)
                queue.append((n_seq, next))

        # 마지막 노드라면 최종적 순서 반환 - 다음노드 추가된게 없을 시
        if not queue:
            return seq


t = int(input()) #테스트케이스 수
for t_seq in range(1, t + 1):
    _, v, e = map(int, input().split()) # 노드, 간선

    # 노드 번호 별 진입차수 저장
    indegrees = [0] * (v + 1)
    indegrees[0] = -1

    # 노드 번호 별 진출노드 저장
    outdegrees = [[] for _ in range(v + 1)]
    
    for _ in range(e):
        a, b = map(int, input().split()) # a -> b 간선
        # 진입차수 + 1
        indegrees[b] += 1

        # 진출노드에 추가
        outdegrees[a].append(b)

    result = topology_sort(v, indegrees, outdegrees)
    
    print(f'{t_seq} {result}')