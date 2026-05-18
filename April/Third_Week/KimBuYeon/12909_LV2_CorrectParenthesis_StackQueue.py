def solution(s):
    stack = []
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')
    for i in range(len(s)):
        if s[i] == "(":
            stack.append(s[i])
        elif s[i] == ")":
            if not stack:
                return False
            else:
                stack.pop()
    if stack:
       return False
    return True