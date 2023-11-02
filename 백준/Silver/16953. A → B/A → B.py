import sys
input = sys.stdin.readline

a, b = map(int, input().split())
answer = 1

'''
- a * 2 와 a * 10 + 1 두개만 가능
- 현재값에서 두가지 경우를 모두 dfs로 호출해서, b이상이 될때까지 반복

'''

def dfs(cur, cnt):
    global answer
    
    if cur >= b:
        if cur == b:
            answer += cnt
        return

    dfs(cur * 2, cnt + 1)
    dfs(cur * 10 + 1, cnt + 1)

dfs(a, 0)

# 만들 수 없을 경우
if answer == 1:
    answer = -1

print(answer)