def solution(genres, plays):
    answer = []
    t_dict, p_dict = {}, {}
    
    # 딕셔너리 - 장르별 재생수 {"classic": 1450, "pop": 3100} {"classic": [(500, 0), (600, 1)]}
    for idx, g in enumerate(genres):
        t_dict[g] = t_dict.get(g, 0) + plays[idx] 
        p_dict[g] = p_dict.get(g, []) + [(plays[idx], idx)]
    
    for genre, _ in sorted(t_dict.items(), key = lambda x: x[1], reverse = True):
        # 장르 내에서 재생횟수(x[0])가 같으면, 고유번호(x[1])이 작은 것부터 오름차순으로 출력해야하니까 -x[1]로 설정
        # {'classic': [(800, 1), (800, 2), (800, 3), (500, 0), (150, 2)]}
        for _, idx in sorted(p_dict[genre], key = lambda x: (x[0], -x[1]), reverse = True)[:2]: #같은 장르에서 최대 2개까지만 추가
            answer.append(idx)
    
    return answer