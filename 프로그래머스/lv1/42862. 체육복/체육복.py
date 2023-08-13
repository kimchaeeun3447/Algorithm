def solution(n, lost, reserve):    
    # 왼, 오 둘다 or 왼쪽에만 lost학생이 있는 경우 = 왼쪽에 옷 줌
    # 오른쪽에만 lost학생이 있는 경우 = 오른쪽에 옷 줌
    
    # 양쪽에 있는 경우 제거
    _reserve = set(reserve) - set(lost)
    _lost = set(lost) - set(reserve)
    
    for r in _reserve:
        if not lost:
            break
        
        if r-1 in _lost:
            _lost.remove(r-1)
        elif r+1 in _lost:
            _lost.remove(r+1)
    
    return n - len(_lost)