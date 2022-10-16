def solution(s):
    conv_num = 0 #변환 횟수
    zero_num = 0 #0의 개수
    answer = []
    
    while (s!='1'):
        conv_num += 1
        zero_num += s.count('0')
        s = list(filter(('0').__ne__, s))
        s = format(len(s), 'b') #2진법   

    answer.append(conv_num)
    answer.append(zero_num)

    return answer
