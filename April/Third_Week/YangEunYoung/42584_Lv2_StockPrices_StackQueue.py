def solution(prices):
    n = len(prices)           
    answer = [0] * n           
    stack = []                 

    for i in range(n):        
        while stack and prices[stack[-1]] > prices[i]:
            past = stack.pop()      
            answer[past] = i - past 
        stack.append(i)

    while stack:
        past = stack.pop()
        answer[past] = (n - 1) - past
        
    return answer
