import sys

input = sys.stdin.readline

n, k = map(int, input().split()) #n개 수 / k개의 연속된 수의 합

tem_list = list(map(int, input().split())) # 1 2 3 4 5 / 2개


#k개의 연속된 수의 합의 결과
result_list = []
result_list.append(sum(tem_list[:k])) # 첫 번째 연속 합으로 초기화

for i in range(n-k):
    # 이전 인덱스 부터 k개 합 - 이전 인덱스 값 + 현재 인덱스에서 k개 맨 끝 값
    tem_sum = result_list[i] - tem_list[i] + tem_list[i+k]
    result_list.append(tem_sum)

print(max(result_list))