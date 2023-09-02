def solution(s):
    answer = True
    stack = []
    
    for a in s:
        if a == "(":
            stack.append("(")
        else:
            if stack:
                stack.pop()
            else:
                # 스택이 비어있다면
                return False
    if stack:
        #"("가 남아있다면
        return False

    return True