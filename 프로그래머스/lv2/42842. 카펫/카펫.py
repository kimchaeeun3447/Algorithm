def solution(brown, yellow):
    answer = []

    # brown - 4 = yellow의 둘레 임을 이용
    # yellow의 가로, 세로 찾음
    r = brown - 4
    for i in range(1, int(yellow**0.5) + 1):
        #i는 세로길이
        if yellow % i == 0:
            if r ==  2 * (yellow // i + i):
                return [yellow // i + 2, i + 2]
    
    '''
    #가로+세로
    s = brown // 2 + 2
    
    #가로*세로
    m = brown + yellow

    # a>=b이고, a+b==s, a*b==m인 a,b구하기
    # 약수 찾기 -> 약수 합 중에 a+b가 충족하는게 있으면 바로 break    
    for i in range(1, int(m**0.5) + 1):
        if m % i == 0 and (m // i + i) == s:
            return([m//i, i])
    '''