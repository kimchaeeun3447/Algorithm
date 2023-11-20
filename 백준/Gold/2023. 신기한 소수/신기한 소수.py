'''
7331 -> 7, 73, 733, 7331 모두 소수인지 판별
'''

# n이 소수인지 판단 - 2부터 n의 제곱근까지 수 중에 약수가 있으면 False 리턴
def is_prime(n):
    if n == 1:
        return False
    
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


# 무조건 소수일 경우에만 재귀가 돌도록
def dfs(n):
    # N자리수가 되면 출력
    if (len(str(n)) == N):
        print(n)

    for i in range(10):
        if (is_prime(n * 10 + i)):
            dfs(n * 10 + i)

# 첫번째 자리수가 소수인 것부터 탐색 시작 -> 9가지 경우의 수에서 4가지로 좁혀짐
N = int(input())
dfs(2); dfs(3); dfs(5); dfs(7)
