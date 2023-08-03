import sys

n, m = map(int, input().split()) # n=표크기(가로,세로 길이) / m=합구해야되는 라인


#원본 배열 입력 받아서 0행, 0열이랑 append
a_list = [[0] * (n+1)] #감싸야되니까 n+1짜리 0행 만듦 [0, 0, 0, 0, 0]


# 0열 만들기위해, 0 다음에 값 append
for _ in range(n):
    #a_row = [0] + list(map(int, input().split()))
    a_row = [0] + list(map(int, sys.stdin.readline().rstrip().split()))
    a_list.append(a_row) #[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4]...]


#합 배열 가공 - 0행, 0열은 어차피 0이니까 1번 인덱스부터 시작
b_list = [[0] * (n+1) for _ in range(n+1)] # n+1 크기의 2차원 배열로 초기화


for x in range(1, n+1):
    for y in range(1, n+1):
        b_list[x][y] = b_list[x-1][y] + b_list[x][y-1] - b_list[x-1][y-1] + a_list[x][y]

# m개의 라인 입력받아서 합 구해서 바로 출력
for _ in range(m):
    #x1, y1, x2, y2 = map(int, input().split())
    x1, y1, x2, y2 = map(int, sys.stdin.readline().rstrip().split())
    result = b_list[x2][y2] - b_list[x1-1][y2] - b_list[x2][y1-1] + b_list[x1-1][y1-1]
    print(result)