#중복순열
from itertools import product

def solution(word):
    answer = 0

    d = sorted([''.join(c) for i in range(5) for c in product("AEIOU", repeat = i + 1)])

    return d.index(word) + 1