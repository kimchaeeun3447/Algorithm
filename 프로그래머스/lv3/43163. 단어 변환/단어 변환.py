from collections import deque

def solution(begin, target, words):
    answer = 0
    visited = {w: False for w in words} #{"hot":False, "dot": False..}
    
    queue = deque([(begin, 0)])
    
    while queue:
        # 큐에 타겟이 있으면 종료
        cur, cnt = queue.popleft()
        if cur == target:
            answer = cnt
            break
        
        visited[cur] = True
        
        for word in words:
            # 이미 방문했으면 패스
            if visited[word]:
                continue
                
            # 한 글자 차이나는 단어들은 queue에 넣음
            diff = 0
            for c, w in zip(cur, word): #"hit", "hot"
                if c != w:
                    diff += 1
    
            if diff == 1:
                queue.append((word, cnt + 1))
        
    return answer