import sys
sys.setrecursionlimit(5000)
n = int(input())


#2

def fibonacci(k):
    if k == 0:
        return 0
    if k == 1:
        return 1
    
    return fibonacci(k-2) + fibonacci(k-1)

print(fibonacci(n))