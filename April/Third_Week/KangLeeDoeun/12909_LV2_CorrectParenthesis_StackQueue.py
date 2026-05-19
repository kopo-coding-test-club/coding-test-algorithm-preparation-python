def solution(s):
    answer = []
    
    for i in s:
        if i == "(":
            answer.append(i)
        
        else:
            if not answer:
                return False
            answer.pop()

    return len(answer) == 0