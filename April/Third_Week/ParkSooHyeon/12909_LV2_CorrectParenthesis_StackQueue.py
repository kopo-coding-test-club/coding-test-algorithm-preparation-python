def solution(s):
    stack = []
    for i in s:
        if len(stack) == 0 and i == ')':
            return False
        
        if i == ')' and stack[-1] == '(':
            stack.pop()

        if i == '(':
            stack.append(i)

    return len(stack) == 0