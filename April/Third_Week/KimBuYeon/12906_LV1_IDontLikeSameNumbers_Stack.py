def solution(arr):
    
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    prev_num = -1
    stack = []
    for i in range(len(arr)):
        if arr[i] != prev_num:
            stack.append(arr[i])
        prev_num = arr[i]
    print('Hello Python')
    return stack