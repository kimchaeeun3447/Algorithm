# 구글링 참고 ㅎ
def solution(numbers):
    answer = ''
    numbers_str = []
    
    for n in numbers:
        numbers_str.append(str(n))
    
    numbers_str.sort(key=lambda n: n * 3, reverse=True)


    return str(int(''.join(numbers_str)))

# # 완전 하드코딩으로 해보기
# from itertools import permutations

# def solution(numbers):
    
#     # 모든 조합 리스트로 넣기
#     numbers_permutations = list(permutations(numbers, len(numbers)))

#     numbers_permutations = list(map(lambda nt: ''.join([str(n) for n in nt]), numbers_permutations))


#     numbers_permutations.sort(reverse=True)

    
#     return numbers_permutations[0]
