def solution(sizes):
    min_size = [min(x, y) for x, y in sizes]
    max_size = [max(x, y) for x, y in sizes]
    
    return max(min_size) * max(max_size)