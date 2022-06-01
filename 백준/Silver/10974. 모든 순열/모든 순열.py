from itertools import permutations

n = int(input())

iterator1 = list(range(1, n+1))

for k in list(permutations(iterator1)):
    for j in k:
        print(j, end=" ")
    print()