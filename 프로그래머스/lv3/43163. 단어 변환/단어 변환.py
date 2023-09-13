'''
- 고민1 : 알파벳이 1개 차이나는 것을 어떻게 파악할지 = begin과 target이 같아질때까지 while 루프 돌게하자.
단어길이가 최대 10이기때문에, for루프를 돌면서 알파벳 차이 개수를 확인한 후 가장 먼저 등장한 word로 변환 = 큐에 삽입한다.

- 고민2 : 조건 - 변환할 수 없는 경우에는 0를 return 합니다. 어떻게 처리할지
다음으로 이동할 알파벳이 한개도 없으면 큐에 삽입이 안되니까, 큐가 비어있으면 자동으로 루프 끝남. answer는 변환 성공했을 경우에만 개수를 초기화한다.

- 처음 런타임 에러 이유: words의 단어들을 재방문못하게 해야함 -> 안그러면 hot 에서 dot으로 안넘어가고 계속 hit을 삽입하게됨(무한루프) 
'''
from collections import deque

def solution(begin, target, words):
    answer = 0
    cnt = 0 # 변환 횟수
    queue = deque([begin]) #변환된 begin을 넣음
    visited = [False] * len(words) #word 방문유무 표시
    length = len(begin)
    
    while queue:
        b = queue.popleft()
        
        # 변환 완료 시 끝
        if b == target:
            answer = cnt
            break
        
        for idx, w in enumerate(words):
            #이미 방문한 word면 패스
            if visited[idx]:
                continue
            
            diff_cnt = 0 # 글자수 차이 계산
            for _w, _b in zip(w, b):
                if _w != _b:
                    diff_cnt += 1
                    
            #글자수 차이가 1개이면 큐에 추가
            if diff_cnt == 1:
                queue.append(w)
                visited[idx] = True
                cnt += 1
                break          
    
    return answer