from itertools import permutations

def solution(numbers):
    result = set()
    
    #자릿수만큼 순열
    for i in range(1, len(numbers) + 1):
        
        # 1)순열 리스트 요소를 문자열로 map -> 2) 문자열을 정수로 map -> 3) 중복제거 -> 4)합집합
        # 장점: 코드가 한 줄됨, 0으로 시작하는 경우 자동으로 제거됨
        # 합집합
        result |= set(map(int, map(''.join, permutations(numbers, i))))
    
    # 0, 1 제거
    result -= set(range(0, 2))

    #아레토스테네스 알고리즘 - 소수 제거
    #2~ 가장 큰 수의 제곱근 수의 배수들이 존재한다면 제거 -> 남은게 소수임
    for i in range(2, int(max(result) ** 0.5) + 1):
        # i의 배수 차집합 - ix2 부터 시작해서 젤 큰 수까지
        result -= set(range(i * 2, max(result) + 1, i))

    return len(result)