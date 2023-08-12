'''
JJJ.AAAAAAAA.KKk
전체길이 14
i=2 - next_i=11

방법1) 오른쪽으로 쭉 이동 : len(name)-1
방법2) 왼쪽부터 시작 : 맨앞에서부터 i만큼 우측이동, 좌측으로 돌아가기(i*2), 맨뒤에서부터 다음 인덱스 next_i까지
이동(len(name)-next_i)
방법3) 오른쪽부터 시작 : 맨뒤에서부터 next_i인덱스까지 좌측이동, 우측으로 돌아가기 2*(len(name)-nex_i)

방법2의 경우 A연속 문자열 양옆중 좌측이 더 적을경우 유리
방법3의 경우 A연속 문자열 양옆중 우측이 더 적을경우 유리

만약 연속 A문자열이 여러 곳에 있어도, 가장 최소 움직임 횟수를 계속 move에 넣기때문에 교체됨

'''

def solution(name):
    #상하 - 최소 알파벳 이동 횟수 찾기
    answer = 0
    
    for a in name:
        # min(상이 유리한 경우, 하가 유리한 경우)
        answer += min(abs(ord("A") - ord(a)), 26 - abs(ord("A") - ord(a)))

    #좌우 - 최소 이동 횟수 찾기
    move = len(name) - 1
    for i, a in enumerate(name):
        # 다음 인덱스부터 연속 A찾으며 그 다음 인덱스 저장
        next_i = i + 1
        while next_i < len(name) and name[next_i] == 'A':
            next_i += 1
        
        move = min(move, i*2 + len(name)-next_i, 2*(len(name)-next_i) + i)
        
    return answer + move