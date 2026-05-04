def solution(arr):
    answer = [arr[0]]
    
    a = arr[0]
    
    for i in arr:
        if a != i:
            answer.append(i)
            a = i

    return answer