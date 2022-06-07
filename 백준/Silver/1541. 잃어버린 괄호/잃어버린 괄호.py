def form(x):
    temp = list(map(lambda x: x.lstrip('0'), x.split('+')))
    return list(map(int, temp))

eList = input().split('-')
numList = []


for e in eList: #['55+9', '50+40']
    temp = form(e)# [55, 9]
    numList.append(sum(temp))

s = numList[0]
for i in range(1, len(numList)):
    s -= numList[i]

print(s)