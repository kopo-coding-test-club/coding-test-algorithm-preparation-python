def solution(sizes):
    answer = 0
    height = []
    width = []
    for w, h in sizes:
        height.append(min(w, h))
        width.append(max(w, h))
    answer = max(height) * max(width)
    return answer
