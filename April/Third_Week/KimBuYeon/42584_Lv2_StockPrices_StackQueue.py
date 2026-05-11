from collections import deque
def solution(prices):
    answer = []
    queue = deque(prices)
    while queue:
        second = 0
        e = queue.popleft()
        for q in queue:
            second += 1
            if e > q:
                break
        answer.append(second)
        
        
        
    return answer