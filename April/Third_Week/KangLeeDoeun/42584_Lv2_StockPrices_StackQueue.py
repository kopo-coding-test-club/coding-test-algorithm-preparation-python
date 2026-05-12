from collections import deque

def solution(prices):
    answer = []
    queue = deque(prices)
    
    # 큐에 담긴게 없을 때 까지
    while queue:
        # 첫번째 요소를 꺼내서
        price = queue.popleft()
        time = 0
        
        # 다음 요소들 하나씩 꺼내고
        for next_price in queue:
            time += 1
            # 나보다 큰 요소가 있으면 break
            if price > next_price: 
                break
        answer.append(time)
        
    return answer