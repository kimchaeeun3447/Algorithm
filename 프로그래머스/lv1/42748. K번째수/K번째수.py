def solution(array, commands):
    answer = []
    
    for command in commands:
        l = array[command[0]-1:command[1]]
        l.sort()
        answer.append(l[command[2]-1])
    return answer