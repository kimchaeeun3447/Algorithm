t = int(input())

# [재귀 이용해서 10진수 -> 2진수 변환 후 LSB부터 1의 위치 세기]
# n==0일 경우 대비 x: n이 0이 아닌 이상, num은 0이 될 수가 없다
# 재귀 종료 : num == 1이 됐을 떄

def getBinaryReverse(num):

    if num == 1:
        return '1'

    # 2로 나눈 나머지에 잇기 = LSB부터 세어야해서 : 순서 뒤집음!
    return str(num % 2) + getBinaryReverse(num // 2)
    #return getBinaryReverse(num // 2) + str(num % 2) -> 이게 맞는 2진수 순서

case = []
for _ in range(t):
    case.append(int(input()))

for n in case:
    b = getBinaryReverse(n)

    for idx, value in enumerate(b):
        if value == '1':
            print(idx, end = ' ')
    print()
