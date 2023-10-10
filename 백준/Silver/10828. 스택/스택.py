import sys
input = sys.stdin.readline

n = int(input())
stack = []
answer = -2

for _ in range(n):
    command = input().split()
    
    if command[0] == 'push':
        stack.append(int(command[1]))
    elif command[0] == 'pop':
        answer = stack.pop() if stack else -1
    elif command[0] == 'size':
        answer = len(stack)
    elif command[0] == 'empty':
        answer = 0 if stack else 1
    else:
        answer = stack[-1] if stack else -1
        
    if command[0] != 'push':
        print(answer)
