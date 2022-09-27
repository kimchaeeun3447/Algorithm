def solution(numbers):
    answer = []
    for a in range(len(numbers)):
        for b in range(a+1, len(numbers)):
            if numbers[a]+numbers[b] not in answer:
                answer.append(numbers[a]+numbers[b])
    
    answer.sort()
    return answer